import faiss
import pickle
import os
from sentence_transformers import SentenceTransformer
from data import data_catalog

# Paths
INDEX_PATH = "catalog_index.faiss"
METADATA_PATH = "catalog_metadata.pkl"
MODEL_NAME = "all-MiniLM-L6-v2"

# Assume data_catalog is defined as before
catalog_texts = [
    f"{entry['table']} - {entry['tabledesc']} Columns: {', '.join(entry['columns'])}"
    for entry in data_catalog
]

# Load model and generate embeddings
model = SentenceTransformer(MODEL_NAME)
embeddings = model.encode(catalog_texts, convert_to_numpy=True)

# Build and save FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)
faiss.write_index(index, INDEX_PATH)

# Save metadata (original data_catalog + model name)
with open(METADATA_PATH, "wb") as f:
    pickle.dump({"catalog": data_catalog, "model_name": MODEL_NAME}, f)

print("✅ Model and index saved.")
