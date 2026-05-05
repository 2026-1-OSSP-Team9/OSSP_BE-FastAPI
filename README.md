# 개요
2026-1 공개 SW 프로젝트 백엔드(FastAPI) 레포지토리입니다.

# 기술스택
- Framework: FastAPI
- Language: Python
- Database: MySQL

# 구조
<!-- START_TREE -->
app
├── api
│   └── v1
│       └── routers.py
├── core
│   ├── config.py
│   ├── logging.py
│   └── security.py
├── crud
│   └── trend.py
├── db
│   ├── base.py
│   └── session.py
├── main.py
├── models
│   └── trend.py
├── services
│   ├── google_trends_scraper.py
│   └── trend_service.py
└── tests
    ├── __init__.py
    ├── test_api.py
    └── test_trend_service.py
<!-- END_TREE -->