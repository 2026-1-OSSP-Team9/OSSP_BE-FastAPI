from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int = 3306
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    DEBUG: bool = False
    SECRET_KEY: str
    SCRAPE_INTERVAL: int = 12
    
    PROJECT_NAME: str = "Google Trends Scraper API"
    
    model_config = SettingsConfigDict(env_file=".env")

    @property
    def DATABASE_URL(self) -> str:
        return f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    # mysql_pymysql://유저명:비밀번호@호스트주소:포트/데이터베이스명
    # 향후 AWS RDS 배포 시에는 아래와 같은 형태 (환경변수 .env로 관리)
    # DATABASE_URL: str = "mysql+pymysql://admin:password1234@my-rds-endpoint.aws.com:3306/trends_db"


settings = Settings()