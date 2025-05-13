# 💡 Korean Product Search (SBERT + ChromaDB)

이 프로젝트는 한국어 상품 설명을 임베딩하여 ChromaDB 벡터 DB에 저장하고,  
사용자의 검색 질의에 대해 의미 기반의 유사도 검색을 수행하는 시맨틱 검색 시스템입니다.

> 📁 이 프로젝트는 비공개 데이터를 기반으로 작동합니다. 데이터 파일은 공유되지 않으며, 예시 구조만 제공됩니다.

> 아래는 예시 구조입니다 :

jsonc
복사
편집
[
  {
    "product_id": "PROD-00001",
    "product_name": "스트레치 Option",
    "category": "패션",
    "subcategory": "신발",
    "brand": "구찌",
    "price": 250000,
    "description": "빈티지한 디자인에 모노톤 요소를 가미한 신발입니다.",
    "rating": 4.9,
    "review_count": 21,
    "stock_status": "일시 품절",
    "feature_tags": ["빈티지", "모노톤", "스웨이드"]
  },
  ...
]



## 📦 프로젝트 구조

```plaintext
.
├── .env                    # 환경변수 설정 파일 (경로 및 설정 값)
├── .gitignore              # 불필요하거나 민감한 파일 제외
├── config.py               # .env 설정을 Python에서 사용하도록 로드
├── common.py               # 모델 로딩 및 ChromaDB 컬렉션 함수
├── 1_embed_products.py     # 상품 설명 임베딩 및 저장
├── 2_save_chromaDB.py      # 저장된 임베딩을 ChromaDB에 저장
├── 3_test_search_chroma.py # 사용자가 질의어를 입력해 유사 상품 검색
├── requirements.txt        # 필요 패키지 목록
├── chroma_store/           # ChromaDB의 로컬 저장소 (Git 제외됨)
└── embeddings.json         # 임베딩된 벡터 파일 (Git 제외됨)

------------------------------------------------------------------------------------------

Python 3.10 이상

가상환경 이름: vector

1. 가상환경 생성 및 활성화
bash
복사
편집
python -m venv vector
source vector/Scripts/activate  # Windows 기준

------------------------------------------------------------------------------------------

2. 의존 패키지 설치
bash
복사
편집
pip install -r requirements.txt

------------------------------------------------------------------------------------------

3. 실행 순서

# 1. 상품 설명 → 벡터 임베딩 후 저장
python 1_embed_products.py

# 2. 벡터를 ChromaDB에 저장
python 2_save_chromaDB.py

# 3. 의미 기반 검색 테스트
python 3_test_search_chroma.py
검색어 예시: "남자 운동화", "고급 가죽 자켓", "스포츠웨어"

------------------------------------------------------------------------------------------


