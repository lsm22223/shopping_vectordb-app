from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoint_search import router as search_router  # ← 본인 파일명대로 유지

app = FastAPI()
app.include_router(search_router, prefix="/api")

#  CORS 허용 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 출처 허용
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)


