# Databricks notebook source
# MAGIC %pip install -r requirements.txt

# COMMAND ----------

import faiss
import sys
import pickle
import os
from sentence_transformers import SentenceTransformer
from raw_data import data_catalog

# COMMAND ----------

# Paths
INDEX_PATH = "catalog_index.faiss"
METADATA_PATH = "catalog_metadata.pkl"
MODEL_NAME = "all-MiniLM-L6-v2"

# COMMAND ----------

def create_catalog_texts(data):
    """Convert database metadata to text format for embedding"""
    catalog_texts = []
    catalog_metadata = []
    
    for database in data:
        for table in database['tables']:
            for column in table['columns']:
                # Create rich text description for each field
                text = f"""Database: {database['database_name']} | Table: {table['table_name']} | Field: {column['field_name']} | Business Name: {column['business_name']} | Description: {column['business_description']} | Type: {column['data_type']} | Tags: {', '.join(column.get('tags', []))}"""
                
                catalog_texts.append(text)
                
                # Store metadata for later retrieval
                metadata = {
                    'database_name': database['database_name'],
                    'database_description': database['database_description'],
                    'table_name': table['table_name'],
                    'table_description': table['table_description'],
                    'field_name': column['field_name'],
                    'business_name': column['business_name'],
                    'business_description': column['business_description'],
                    'data_type': column['data_type'],
                    'length': column.get('length'),
                    'tags': column.get('tags', []),
                    'sample_values': column.get('sample_values', [])
                }
                catalog_metadata.append(metadata)
    
    return catalog_texts, catalog_metadata

# COMMAND ----------

def main():
    # # Load database metadata
    # print("Loading database metadata...")
    # data = json.loads(json_data)
    
    # Create catalog texts for embedding
    print("Creating catalog texts...")
    catalog_texts, catalog_metadata = create_catalog_texts(data_catalog)
    
    print(f"Generated {len(catalog_texts)} field descriptions")
    
    # Load model and generate embeddings
    print("Loading SentenceTransformer model...")
    model = SentenceTransformer(MODEL_NAME)
    
    print("Generating embeddings...")
    embeddings = model.encode(catalog_texts, convert_to_numpy=True)
    
    print(f"Generated embeddings shape: {embeddings.shape}")
    
    # Build and save FAISS index
    print("Building FAISS index...")
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    faiss.write_index(index, INDEX_PATH)
    
    # Save metadata
    print("Saving metadata...")
    metadata_to_save = {
        "catalog_metadata": catalog_metadata,
        "catalog_texts": catalog_texts,
        "model_name": MODEL_NAME
    }
    
    with open(METADATA_PATH, "wb") as f:
        pickle.dump(metadata_to_save, f)
    
    print("✅ Model and index saved successfully!")
    print(f"Index saved to: {INDEX_PATH}")
    print(f"Metadata saved to: {METADATA_PATH}")
    
    # Test the index with a sample query
    print("\n🧪 Testing with sample queries...")
    test_queries = [
        "customer name",
        "account number", 
        "phone number",
        "transaction date"
    ]
    
    for query in test_queries:
        print(f"\nQuery: '{query}'")
        query_embedding = model.encode([query], convert_to_numpy=True)
        
        # Search in index
        distances, indices = index.search(query_embedding, k=3)
        
        print("Top 3 matches:")
        for i, (distance, idx) in enumerate(zip(distances[0], indices[0])):
            metadata = catalog_metadata[idx]
            print(f"  {i+1}. {metadata['database_name']}.{metadata['table_name']}.{metadata['field_name']} - {metadata['business_name']} (distance: {distance:.3f})")

# COMMAND ----------

if __name__ == "__main__":
    main()
