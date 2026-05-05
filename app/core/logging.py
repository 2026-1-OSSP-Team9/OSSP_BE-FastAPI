import logging
import os

# 로그 파일 경로
LOG_FILE_PATH = "logs/app.log"
os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True) # logs 폴더 생성

# 기본 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(), # 터미널 출력
        logging.FileHandler(LOG_FILE_PATH, mode="a") # 파일 저장
    ]
)

# 로거 가져오기
logger = logging.getLogger("fastapi_app")
logger.info("로깅 설정 완료")