from sentence_transformers import SentenceTransformer
import chromadb
from config import MODEL_NAME, CHROMA_DIR

def load_model():
    return SentenceTransformer(MODEL_NAME)

def get_chroma_collection():
    client = chromadb.PersistentClient(path=CHROMA_DIR)
    collection = client.get_or_create_collection(
        name="products",
        metadata={"hnsw:space": "cosine"}
    )
    return collection
