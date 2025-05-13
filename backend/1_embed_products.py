import json
from common import load_model
from config import DATA_PATH, SAVE_EMB_PATH, BATCH_SIZE

# 모델 로드
model = load_model()

# 데이터 불러오기
with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

documents = [item["description"] for item in data]

# 임베딩 수행
print(" 문장 임베딩 중...")
embeddings = model.encode(documents, batch_size=BATCH_SIZE, show_progress_bar=True)

# JSON 저장
with open(SAVE_EMB_PATH, "w", encoding="utf-8") as f:
    json.dump(embeddings.tolist(), f)

print(f" 임베딩 저장 완료 → {SAVE_EMB_PATH}")
