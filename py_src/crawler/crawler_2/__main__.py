from core.logger import get_my_logger
from crawler_2.task import MUSIC_URLS, download

logger = get_my_logger("task")

if __name__ == "__main__":
    logger.info("[main start]")
    # 크롤링 대상 URL 별로 download() 함수를 태스크로 큐에 넣음
    # 큐에 들어간 태스크는 워커에 의해서 자동 실행됨
    for music_url in MUSIC_URLS:
        download.delay(music_url)
    logger.info("[main finished]")
