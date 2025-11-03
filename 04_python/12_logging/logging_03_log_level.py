import logging  # logging 표준 라이브러리를 사용한다.
from logging import LogRecord

class DefatultClass:
    def log_level():
        # 기본적인 사용법
        logger_name = "log_level"             # 로거 이름 설정
        filename = "log/log_level_log.log"    # 로그를 기록할 파일 경로 설정

        # 로거 객체를 생성
        logger = logging.getLogger(logger_name)

        # 로깅 설정 (전역, 1회만)
        logging.basicConfig(filename=filename, level=logging.INFO, encoding='utf-8')

        # 로그 레벨
        # 로그 레벨은 기본적으로 6개의 단계로 이루어져 있다.
        # 이 중 NOTSET 은 로거를 생성할 때의 초기 로깅 레벨이며
        # FATAL은 CRITICAL과, WARN 은 WARNING 과 같은 레벨이다.
        # 이들은 정수값을 가지고 있다. (enum 스타일)
        """
        # logging.__init__
        CRITICAL = 50
        FATAL = CRITICAL
        ERROR = 40
        WARNING = 30
        WARN = WARNING
        INFO = 20
        DEBUG = 10
        NOTSET = 0
        """

        # 로그 메시지를 기록한다.
        # 설정한 level 미만의 로그는 기록되지 않는다.
        logger.info("info 메시지입니다.")
        logger.debug("debug 메시지입니다.")
        logger.warning("warning 메시지입니다.")
        logger.error("error 메시지입니다.")
        
        
        