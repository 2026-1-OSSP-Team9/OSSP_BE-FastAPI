import requests
import xml.etree.ElementTree as ET
from core.logging import logger

class GoogleTrendsScraper:
    def __init__(self):
        self.url = "https://trends.google.com/trending/rss?geo=KR"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36..."
        }

    def fetch_trends(self) -> list[str]:
        """구글에서 RSS를 가져와 키워드 리스트만 반환"""
        try:
            response = requests.get(self.url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return self._parse_xml(response.content)
        except Exception as e:
            logger.error(f"스크래핑 중 오류 발생: {e}")
            return []

    def _parse_xml(self, content: bytes) -> list[str]:
        root = ET.fromstring(content)
        return [item.find("title").text for item in root.findall(".//item") if item.find("title") is not None]