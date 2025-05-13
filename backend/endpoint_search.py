from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from typing import Optional
import numpy as np

from common import load_model, get_chroma_collection

router = APIRouter()
model = load_model()
collection = get_chroma_collection()


def cosine_similarity(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))


@router.get("/search")
def search_products(
    q: Optional[str] = Query(None, description="검색어 (예: 운동화)"),
    top_k: int = Query(3, ge=1, le=10, description="검색 결과 수 (1~10)")
):
    print("▶ 수신된 q 값:", repr(q))  # 디버깅 로그

    if not q or not q.strip():
        return JSONResponse(
            status_code=422,
            content={"detail": "'q' 검색어는 비워둘 수 없습니다. 예: ?q=운동화"}
        )

    try:
        query_vec = model.encode([q])[0].tolist()

        results = collection.query(
            query_embeddings=[query_vec],
            n_results=top_k,
            include=["documents", "metadatas", "embeddings", "distances"]
        )

        return {
            "query": q,
            "results": [
                {
                    "id": results["ids"][0][i],
                    "description": results["documents"][0][i],
                    "metadata": {
                        **{k: v for k, v in results["metadatas"][0][i].items() if k != "description"}
                    },
                    "cosine_similarity": cosine_similarity(query_vec, results["embeddings"][0][i]),
                    "l2_distance": results["distances"][0][i]
                }
                for i in range(len(results["ids"][0]))
            ]
        }

    except Exception as e:
        print(" 검색 실패:", e)
        return JSONResponse(status_code=500, content={"error": str(e)})
