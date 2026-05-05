import pytest
from sqlalchemy.orm import Session
from db.session import SessionLocal
from models.trend import Trend
from services.trend_service import get_google_trends

# 실제 Google Trends API를 호출하고 로컬 MySQL DB에 적재되는지 확인하는 통합 테스트
def test_get_google_trends():
    db: Session = SessionLocal()
    
    try:
        # 1. 테스트 전 기존 데이터 개수 확인
        initial_count = db.query(Trend).count()
        print(f"\n[테스트 시작] 현재 DB 데이터 개수: {initial_count}")
        
        # 2. 실제 수집 및 저장 함수 실행
        get_google_trends(db=db)
        
        # 3. DB 상태 강제 새로고침
        db.expire_all() # 테스트 세션은 함수 내부에서 일어난 변화를 즉시 모를 수 있으므로 expire_all 사용
        new_count = db.query(Trend).count()
        print(f"[수집 완료] 수집 후 DB 데이터 개수: {new_count}")
        
        # 4. 검증: 데이터가 최소 1개 이상 추가되었는가?
        # 만약 여기서 에러가 난다면 get_google_trends()가 구글에서 데이터를 못 가져온 것
        assert new_count > initial_count, f"DB에 데이터가 추가되지 않았습니다. (이전: {initial_count}, 현재: {new_count})"
        
        # 5. 저장된 데이터 샘플 확인
        latest_trend = db.query(Trend).order_by(Trend.fetched_at.desc()).first()
        if latest_trend:
            print(f"최신 수집 키워드 확인 성공: {latest_trend.keyword}")
            assert latest_trend.keyword is not None
        
    except Exception as e:
        print(f"테스트 중 예외 발생: {e}")
        raise e
        
    finally:
        db.close()