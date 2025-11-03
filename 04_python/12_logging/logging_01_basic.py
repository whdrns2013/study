import logging  # logging 표준 라이브러리를 사용한다.

class DefatultClass:
    def logging_basic():
        # 기본적인 사용법
        logger_name = "logging_basic"             # 로거 이름 설정
        filename = "log/logging_basic_log.log"    # 로그를 기록할 파일 경로 설정

        # 로거 객체를 생성
        logger = logging.getLogger(logger_name)

        # 로깅 설정 (전역, 1회만)
        logging.basicConfig(filename=filename, level=logging.DEBUG, encoding='utf-8')

        # 로그 메시지를 기록한다.
        logger.info("info 메시지입니다.")
        logger.debug("debug 메시지입니다.")
        logger.warning("warning 메시지입니다.")
        logger.error("error 메시지입니다.")