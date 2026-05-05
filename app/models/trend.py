from sqlalchemy import Column ,Integer, String, DateTime
from datetime import datetime
from db.base import Base

# 구글 트렌드 키워드
class Trend(Base):
    __tablename__ = "trend"

    id = Column(Integer, primary_key=True, index=True)
    keyword = Column(String(255), index=True)
    rank = Column(Integer)
    fetched_at = Column(DateTime, default=datetime.utcnow)