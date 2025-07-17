# Load everything
import faiss
import pickle
import os
import numpy as np
from sentence_transformers import SentenceTransformer
from data import data_catalog



# Paths
INDEX_PATH = "catalog_index.faiss"
METADATA_PATH = "catalog_metadata.pkl"
MODEL_NAME = "all-MiniLM-L6-v2"


def load_catalog_assistant(index_path=INDEX_PATH, metadata_path=METADATA_PATH):
    # Load FAISS index
    index = faiss.read_index(index_path)
    
    # Load metadata and model
    with open(metadata_path, "rb") as f:
        metadata = pickle.load(f)
    
    model = SentenceTransformer(metadata["model_name"])
    data_catalog = metadata["catalog"]
    
    return model, index, data_catalog

# Search function
def search_catalog(query, model, index, data_catalog, top_k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)
    results = [data_catalog[i] for i in indices[0]]
    return results

# Example usage
model, index, data_catalog = load_catalog_assistant()
query = input("Ask you question : ")
results = search_catalog(query, model, index, data_catalog)

for res in results:
    print(f"\nTable: {res['table']}")
    print(f"Description: {res['tabledesc']}")
    print(f"Columns: {', '.join(res['columns'])}")
