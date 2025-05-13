import json
from common import get_chroma_collection
from config import DATA_PATH, SAVE_EMB_PATH, BATCH_SIZE

# 데이터 및 임베딩 불러오기
with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

with open(SAVE_EMB_PATH, "r", encoding="utf-8") as f:
    embeddings = json.load(f)

documents = [item["description"] for item in data]
ids = [item["product_id"] for item in data]

# 메타데이터 정제 함수
def sanitize_metadata(item):
    return {k: (", ".join(v) if isinstance(v, list) else v) for k, v in item.items() if k != "description"}

metadatas = [sanitize_metadata(item) for item in data]

# ChromaDB 저장
collection = get_chroma_collection()
print(" ChromaDB 저장 시작...")

for i in range(0, len(documents), BATCH_SIZE):
    collection.add(
        documents=documents[i:i + BATCH_SIZE],
        embeddings=embeddings[i:i + BATCH_SIZE],
        metadatas=metadatas[i:i + BATCH_SIZE],
        ids=ids[i:i + BATCH_SIZE]
    )
    print(f" {min(i + BATCH_SIZE, len(documents))} / {len(documents)} 저장됨")

print(" 저장 완료!")
