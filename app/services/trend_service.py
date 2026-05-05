from sqlalchemy.orm import Session
from db.session import SessionLocal
from crud.trend import create_trends
from core.logging import logger
from .google_trends_scraper import GoogleTrendsScraper

def get_google_trends(db: Session = None):
    # db가 없으면 새로 만들고(스케줄러용), 있으면 사용(테스트용)
    is_local_session = False
    if db is None:
        db = SessionLocal()
        is_local_session = True

    try:
        scraper = GoogleTrendsScraper()
        keywords = scraper.fetch_trends()

        if keywords:
            create_trends(db, keywords)
            logger.info(f"성공적으로 {len(keywords)}개의 트렌드를 저장했습니다.")
    finally:
        if is_local_session:
            db.close()