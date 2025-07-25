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

def search_catalog_conversational(query, model, index, catalog_metadata, catalog_texts, top_k=5):
    """Conversational search using FAISS and semantic embeddings"""
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

    return generate_conversational_response(query, results)

# COMMAND ----------

def generate_conversational_response(query, results):
    if not results:
        return {
            'message': f"I couldn't find anything related to '{query}' in our data catalog. Try being more specific.",
            'results': []
        }

    opening = f"I found {len(results)} fields related to '{query}':"

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
        'message': opening,
        'results': formatted_results
    }

# COMMAND ----------

def chat_with_catalog(query, model, index, catalog_metadata, catalog_texts):
    response = search_catalog_conversational(query, model, index, catalog_metadata, catalog_texts)
    print(f"\n🤖 {response['message']}\n")
    for r in response['results']:
        print(f"{r['rank']}. {r['description']}\n")

# COMMAND ----------

def main():
    print("🚀 Conversational Metadata Search")
    model, index, catalog_metadata, catalog_texts = load_catalog_assistant()

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
