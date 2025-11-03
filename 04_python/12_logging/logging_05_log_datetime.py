import logging  # logging 표준 라이브러리를 사용한다.
import time

class DefatultClass:
    def log_datetime():
        # 기본적인 사용법
        logger_name = "log_datetime"             # 로거 이름 설정
        filename = "log/log_datetime_log.log"    # 로그를 기록할 파일 경로 설정

        # 로거 객체를 생성
        logger = logging.getLogger(logger_name)

        # 로깅 설정 (전역, 1회만)
        logging.basicConfig(filename=filename,
                            level=logging.DEBUG,
                            encoding='utf-8',
                            format="%(asctime)s : %(message)s")

        # 로그 메시지를 기록한다.
        logger.info("datetime 을 로깅해보았습니다.")
        time.sleep(0.1)
        logger.info("이것은 Textual time when the LogRecord was created에 해당합니다.")