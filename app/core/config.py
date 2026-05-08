from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # 1. Railway가 자동으로 주입해 줄 변수 (로컬엔 없으므로 Optional)
    MYSQL_URL: Optional[str] = None

    # 2. 로컬용 변수들 (Railway 배포 시 필수값 에러가 나지 않도록 Optional 및 기본값 세팅)
    DB_HOST: Optional[str] = "localhost"
    DB_PORT: int = 3306
    DB_USER: Optional[str] = "root"
    DB_PASSWORD: Optional[str] = ""
    DB_NAME: Optional[str] = "lawlink"

    DEBUG: bool = False
    SECRET_KEY: str = "default_secret" 
    SCRAPE_INTERVAL: int = 12
    
    PROJECT_NAME: str = "Google Trends Scraper API"
    
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def get_database_url(self) -> str:
        # A. Railway 등 배포 환경: MYSQL_URL이 존재할 경우
        if self.MYSQL_URL:
            url = self.MYSQL_URL
            # SQLAlchemy 호환성을 위해 mysql:// 을 mysql+pymysql:// 로 자동 변환
            if url.startswith("mysql://"):
                url = url.replace("mysql://", "mysql+pymysql://", 1)
            return url
        
        # B. 로컬 환경: 개별 변수들을 조립해서 사용
        return f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # mysql_pymysql://유저명:비밀번호@호스트주소:포트/데이터베이스명
    # 향후 AWS RDS 배포 시에는 아래와 같은 형태 (환경변수 .env로 관리)
    # DATABASE_URL: str = "mysql+pymysql://admin:password1234@my-rds-endpoint.aws.com:3306/trends_db"


settings = Settings()
