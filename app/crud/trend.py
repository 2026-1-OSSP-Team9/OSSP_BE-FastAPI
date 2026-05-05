from sqlalchemy.orm import Session
from models.trend import Trend
from datetime import datetime, timezone
from core.logging import logger

# Trend 데이터 삽입
def create_trends(db: Session, keywords: list[str]):
    try:
        if not keywords:
            print("💾 저장할 키워드가 없습니다.")
            return

        trends_to_insert = []
        for rank, keyword in enumerate(keywords, start=1):
            trend = Trend(
                keyword=keyword,
                rank=rank,
                fetched_at=datetime.now(timezone.utc)
            )
            trends_to_insert.append(trend)

        db.add_all(trends_to_insert)
        db.commit()
        logger.info(f"DB 적재 완료: {len(trends_to_insert)}건")
    except Exception as e:
        db.rollback() # 에러 발생 시 되돌리기
        logger.error(f"DB 저장 오류: {e}")
        raise e