from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# 엔드포인트 살아있는지 테스트
def test_app_is_running():
    # 루트 엔드포인트 GET 요청
    response = client.get("/")

    # HTTP 상태 코드가 200인지 확인
    assert response.status_code == 200
    # 반환되는 JSON 데이터가 맞는지 확인
    assert response.json() == {"message": "Google Trends Scraper is running"}