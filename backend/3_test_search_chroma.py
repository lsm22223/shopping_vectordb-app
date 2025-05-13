from common import load_model, get_chroma_collection
from config import BATCH_SIZE
import numpy as np

model = load_model()
collection = get_chroma_collection()

print(f" 현재 저장된 벡터 수: {collection.count()}")

def cosine_similarity(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

def search(query, top_k=3):
    query_vec = model.encode([query])[0].tolist()
    results = collection.query(
        query_embeddings=[query_vec],
        n_results=top_k,
        include=["documents", "metadatas", "embeddings", "distances"]
    )

    if not results["ids"] or not results["ids"][0]:
        print(" 검색 결과 없음")
        return

    for i in range(len(results["ids"][0])):
        emb = results['embeddings'][0][i]
        cosine_sim = cosine_similarity(query_vec, emb)
        l2_dist = results['distances'][0][i]
        metadata = {k: v for k, v in results['metadatas'][0][i].items() if k != "description"}

        print(f"\n🔹 Result {i+1}")
        print(f"1. Product ID: {results['ids'][0][i]}")
        print(f"2. Description: {results['documents'][0][i]}")
        print(f"3. Metadata: {metadata}")
        print(f"4. L2 Distance: {l2_dist:.4f}")
        print(f"5. Cosine Similarity: {cosine_sim:.4f}")

if __name__ == "__main__":
    query = input(" 검색어 입력: ")
    search(query)
