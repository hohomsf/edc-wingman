# Databricks notebook source
# MAGIC %pip install -r requirements.txt

# COMMAND ----------

# Load everything
import faiss
import pickle
import os
import numpy as np
from sentence_transformers import SentenceTransformer
from raw_data import data_catalog
from intent_examples import intent_examples

# COMMAND ----------

# Paths
INDEX_PATH = "catalog_index.faiss"
METADATA_PATH = "catalog_metadata.pkl"
MODEL_NAME = "all-MiniLM-L6-v2"

# COMMAND ----------

def load_catalog_assistant(index_path=INDEX_PATH, metadata_path=METADATA_PATH):
    """Load the trained model, FAISS index, and metadata"""
    if not os.path.exists(index_path):
        raise FileNotFoundError(f"Index file not found: {index_path}. Please run train_model.py first.")

    if not os.path.exists(metadata_path):
        raise FileNotFoundError(f"Metadata file not found: {metadata_path}. Please run train_model.py first.")

    print("Loading FAISS index...")
    index = faiss.read_index(index_path)

    print("Loading metadata...")
    with open(metadata_path, "rb") as f:
        metadata = pickle.load(f)

    print(f"Loading SentenceTransformer model: {metadata['model_name']}")
    model = SentenceTransformer(metadata["model_name"])

    catalog_metadata = metadata["catalog_metadata"]
    catalog_texts = metadata["catalog_texts"]

    print(f"✅ Loaded {len(catalog_metadata)} database fields")

    return model, index, catalog_metadata, catalog_texts

# COMMAND ----------

def detect_intent(query, model):
    """Detect user intent based on semantic similarity to intent examples"""
    query_embedding = model.encode([query])
    
    intent_scores = {}
    
    for intent, examples in intent_examples.items():
        example_embeddings = model.encode(examples)
        similarities = np.dot(query_embedding, example_embeddings.T).flatten()
        intent_scores[intent] = np.max(similarities)  # Take the highest similarity
    
    # Get the intent with highest score
    detected_intent = max(intent_scores, key=intent_scores.get)
    confidence = intent_scores[detected_intent]
    
    # Set a threshold for intent detection confidence
    if confidence < 0.3:  # Adjust threshold as needed
        detected_intent = "field"  # Default to field-level search
    
    return detected_intent, confidence

# COMMAND ----------

def get_database_level_response(catalog_metadata):
    """Generate database-level summary"""
    databases = {}
    for meta in catalog_metadata:
        db_name = meta['database_name']
        if db_name not in databases:
            databases[db_name] = {'tables': set(), 'field_count': 0}
        databases[db_name]['tables'].add(meta['table_name'])
        databases[db_name]['field_count'] += 1
    
    results = []
    for db_name, info in databases.items():
        desc = f"**{db_name}** database\n   📊 {len(info['tables'])} tables, {info['field_count']} fields total"
        results.append({
            'rank': len(results) + 1,
            'description': desc
        })
    
    return {
        'message': f"I found {len(databases)} databases in our catalog:",
        'results': results
    }

# COMMAND ----------

def get_table_level_response(query, model, index, catalog_metadata, catalog_texts, top_k=10):
    """Generate table-level summary"""
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k * 3)  # Get more results to aggregate
    
    tables = {}
    for distance, idx in zip(distances[0], indices[0]):
        meta = catalog_metadata[idx]
        table_key = f"{meta['database_name']}.{meta['table_name']}"
        
        if table_key not in tables:
            tables[table_key] = {
                'database': meta['database_name'],
                'table': meta['table_name'],
                'fields': [],
                'total_score': 0,
                'field_count': 0
            }
        
        tables[table_key]['fields'].append({
            'field': meta['field_name'],
            'business_name': meta['business_name'],
            'score': 1 / (1 + distance)
        })
        tables[table_key]['total_score'] += 1 / (1 + distance)
        tables[table_key]['field_count'] += 1
    
    # Sort tables by relevance score
    sorted_tables = sorted(tables.values(), key=lambda x: x['total_score'], reverse=True)[:top_k]
    
    results = []
    for i, table_info in enumerate(sorted_tables):
        top_fields = sorted(table_info['fields'], key=lambda x: x['score'], reverse=True)[:3]
        field_list = ", ".join([f['business_name'] or f['field'] for f in top_fields])
        
        desc = (f"**{table_info['table']}** in `{table_info['database']}` database\n"
                f"   📊 {table_info['field_count']} relevant fields\n"
                f"   🔝 Top fields: {field_list}")
        
        results.append({
            'rank': i + 1,
            'description': desc
        })
    
    return {
        'message': f"I found {len(results)} relevant tables for '{query}':",
        'results': results
    }

# COMMAND ----------

def get_field_level_response(query, model, index, catalog_metadata, catalog_texts, top_k=5):
    """Generate detailed field-level response (original functionality)"""
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)

    results = []
    for i, (distance, idx) in enumerate(zip(distances[0], indices[0])):
        meta = catalog_metadata[idx]
        result = {
            'rank': i + 1,
            'database': meta['database_name'],
            'table': meta['table_name'],
            'field': meta['field_name'],
            'business_name': meta['business_name'],
            'business_description': meta['business_description'],
            'data_type': meta['data_type'],
            'tags': meta.get('tags', []),
            'sample_values': meta.get('sample_values', []),
            'score': 1 / (1 + distance)
        }
        results.append(result)

    return generate_field_level_display(query, results)

# COMMAND ----------

def generate_field_level_display(query, results):
    """Format field-level results for display"""
    if not results:
        return {
            'message': f"I couldn't find any fields related to '{query}' in our data catalog. Try being more specific.",
            'results': []
        }

    formatted_results = []
    for r in results:
        desc = (
            f"**{r['business_name']}** (`{r['field']}`) in table `{r['table']}` of database `{r['database']}`\n"
            f"   📝 {r['business_description']}\n"
            f"   🏷️ Type: {r['data_type']}\n"
        )
        if r['tags']:
            desc += f"   🔖 Tags: {', '.join(r['tags'])}\n"
        if r['sample_values']:
            desc += f"   📋 Samples: {', '.join(r['sample_values'][:3])}\n"

        formatted_results.append({
            'rank': r['rank'],
            'description': desc.strip()
        })

    return {
        'message': f"I found {len(results)} fields related to '{query}':",
        'results': formatted_results
    }

# COMMAND ----------

def search_catalog_conversational(query, model, index, catalog_metadata, catalog_texts, top_k=5):
    """Conversational search with intent detection"""
    # Detect user intent
    intent, confidence = detect_intent(query, model)
    
    print(f"🎯 Detected intent: {intent} (confidence: {confidence:.2f})")
    
    # Route to appropriate response generator based on intent
    if intent == "database":
        return get_database_level_response(catalog_metadata)
    elif intent == "table":
        return get_table_level_response(query, model, index, catalog_metadata, catalog_texts, top_k)
    else:  # field level (default)
        return get_field_level_response(query, model, index, catalog_metadata, catalog_texts, top_k)

# COMMAND ----------

def chat_with_catalog(query, model, index, catalog_metadata, catalog_texts):
    """Main chat interface with enhanced intent-based responses"""
    response = search_catalog_conversational(query, model, index, catalog_metadata, catalog_texts)
    print(f"\n🤖 {response['message']}\n")
    for r in response['results']:
        print(f"{r['rank']}. {r['description']}\n")

# COMMAND ----------

def main():
    print("🚀 Enhanced Conversational Metadata Search with Intent Detection")
    model, index, catalog_metadata, catalog_texts = load_catalog_assistant()

    print("\n💡 Try different types of queries:")
    print("   📊 Database level: 'What databases do we have?'")
    print("   📋 Table level: 'What tables are in the CUST database?'")
    print("   🔍 Field level: 'Where is customer name stored?'")

    while True:
        query = input("\n🔍 Enter your search query (or 'quit' to exit): ").strip()
        if query.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break
        elif not query:
            print("❌ Please enter a valid query")
        else:
            chat_with_catalog(query, model, index, catalog_metadata, catalog_texts)

# COMMAND ----------

if __name__ == "__main__":
    main()
