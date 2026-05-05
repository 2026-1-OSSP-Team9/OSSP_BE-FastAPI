from fastapi import FastAPI
from contextlib import asynccontextmanager
from apscheduler.schedulers.background import BackgroundScheduler
from db.session import engine
from db.base import Base
from services.trend_service import get_google_trends

# DB 생성
Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 스케줄러 초기화
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_google_trends, "interval", hours=12) # interval, 12시간 간격
    scheduler.start()

    # 앱 구동 직후 즉시 1회 실행
    get_google_trends()

    yield

    # 앱 종료 시 스케줄러 종료
    scheduler.shutdown()

app = FastAPI(title="Google Trends Scraper API", lifespan=lifespan)

@app.get("/")
def root():
    return {"message": "Google Trends Scraper is running"}