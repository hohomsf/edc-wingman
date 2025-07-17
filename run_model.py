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
    
    # Check if files exist
    if not os.path.exists(index_path):
        raise FileNotFoundError(f"Index file not found: {index_path}. Please run train_model.py first.")
    
    if not os.path.exists(metadata_path):
        raise FileNotFoundError(f"Metadata file not found: {metadata_path}. Please run train_model.py first.")
    
    # Load FAISS index
    print("Loading FAISS index...")
    index = faiss.read_index(index_path)
    
    # Load metadata and model
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

# Search function
def search_catalog(query, model, index, catalog_metadata, catalog_texts, top_k=5):
    """Search for similar database fields based on query"""
    
    print(f"🔍 Searching for: '{query}'")
    
    # Generate embedding for the query
    query_embedding = model.encode([query])
    
    # Search in the index
    distances, indices = index.search(np.array(query_embedding), top_k)
    
    # Get results with metadata
    results = []
    for i, (distance, idx) in enumerate(zip(distances[0], indices[0])):
        result = {
            'rank': i + 1,
            'distance': distance,
            'metadata': catalog_metadata[idx],
            'text': catalog_texts[idx],
            'similarity_score': 1 / (1 + distance)  # Convert distance to similarity score
        }
        results.append(result)
    
    return results

# COMMAND ----------

def display_results(results):
    """Display search results in a formatted way"""
    
    print("\n" + "="*80)
    print("🎯 SEARCH RESULTS")
    print("="*80)
    
    for result in results:
        metadata = result['metadata']
        
        print(f"\n📌 Rank {result['rank']} | Similarity: {result['similarity_score']:.3f}")
        print("-" * 60)
        print(f"🏛️  Database: {metadata['database_name']}")
        print(f"📊 Table: {metadata['table_name']}")
        print(f"🔤 Field: {metadata['field_name']}")
        print(f"💼 Business Name: {metadata['business_name']}")
        print(f"📝 Description: {metadata['business_description']}")
        print(f"🏷️  Type: {metadata['data_type']} ({metadata.get('length', 'N/A')})")
        
        if metadata.get('tags'):
            print(f"🏷️  Tags: {', '.join(metadata['tags'])}")
        
        if metadata.get('sample_values'):
            sample_display = ', '.join(metadata['sample_values'][:3])  # Show first 3 samples
            if len(metadata['sample_values']) > 3:
                sample_display += "..."
            print(f"📋 Sample Values: {sample_display}")
        
        print(f"📏 Distance: {result['distance']:.4f}")

# COMMAND ----------

def interactive_search():
    """Interactive search interface"""
    
    print("🚀 Database Metadata Search System")
    print("=" * 50)
    
    try:
        # Load the model and index
        model, index, catalog_metadata, catalog_texts = load_catalog_assistant()
        
        print("\n💡 Try searching for:")
        print("   - 'customer name'")
        print("   - 'account number'")
        print("   - 'phone number'")
        print("   - 'transaction date'")
        print("   - 'personal information'")
        print("   - 'PII data'")
        print("\n" + "-" * 50)
        
        while True:
            query = input("\n🔍 Enter your search query (or 'quit' to exit): ").strip()
            
            if query.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if not query:
                print("❌ Please enter a valid query")
                continue
            
            try:
                # Search for similar fields
                results = search_catalog(query, model, index, catalog_metadata, catalog_texts)
                
                # Display results
                display_results(results)
                
                # Ask if user wants to see more results
                while True:
                    more = input("\n🔄 Show more results? (y/n): ").strip().lower()
                    if more in ['y', 'yes']:
                        more_results = search_catalog(query, model, index, catalog_metadata, catalog_texts, top_k=10)
                        display_results(more_results[5:])  # Show next 5 results
                        break
                    elif more in ['n', 'no']:
                        break
                    else:
                        print("Please enter 'y' or 'n'")
                
            except Exception as e:
                print(f"❌ Error during search: {e}")
    
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        print("Please make sure you have run train_model.py first!")

# COMMAND ----------

def batch_search(queries, top_k=3):
    """Search multiple queries at once"""
    
    print("🔍 Batch Search Mode")
    print("=" * 30)
    
    try:
        model, index, catalog_metadata, catalog_texts = load_catalog_assistant()
        
        for query in queries:
            print(f"\n{'='*60}")
            print(f"Query: '{query}'")
            print('='*60)
            
            results = search_catalog(query, model, index, catalog_metadata, catalog_texts, top_k=top_k)
            
            for result in results:
                metadata = result['metadata']
                print(f"\n{result['rank']}. {metadata['database_name']}.{metadata['table_name']}.{metadata['field_name']}")
                print(f"   Business Name: {metadata['business_name']}")
                print(f"   Description: {metadata['business_description']}")
                print(f"   Similarity: {result['similarity_score']:.3f}")
    
    except Exception as e:
        print(f"❌ Error: {e}")

# COMMAND ----------

def main():
    """Main function with different modes"""
    
    print("Welcome to Database Metadata Search!")
    print("Choose a mode:")
    print("1. Interactive Search")
    print("2. Batch Search (predefined queries)")
    print("3. Single Query")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        interactive_search()
    
    elif choice == "2":
        # Predefined queries for batch search
        test_queries = [
            "customer name",
            "account number",
            "phone number",
            "transaction date",
            "personal information",
            "PII data",
            "customer identification",
            "account details"
        ]
        batch_search(test_queries)
    
    elif choice == "3":
        try:
            model, index, catalog_metadata, catalog_texts = load_catalog_assistant()
            query = input("Enter your search query: ")
            results = search_catalog(query, model, index, catalog_metadata, catalog_texts)
            display_results(results)
        except Exception as e:
            print(f"❌ Error: {e}")
    
    else:
        print("Invalid choice. Please run the script again.")

# COMMAND ----------

if __name__ == "__main__":
    main()
