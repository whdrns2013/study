import logging
from logging import LogRecord

def log_level_test():

    # 로거 객체를 생성
    logger_name = "log_level"
    logger = logging.getLogger(logger_name)

    # 로깅 설정
    filename = "logs/log_level_log.log"
    logging.basicConfig(filename=filename,
                        level=logging.INFO, # 로거가 처리할 최소의 로그 레벨을 INFO 로 정함
                        encoding='utf-8')

    # 로그 레벨은 기본적으로 6개의 단계로 이루어져 있다.  
    # 그리고 이들은 정수값을 가지고 있다.
    # logging.__init__.py 파일에서 자세하게 살펴볼 수 있다.  
    """
    CRITICAL = FATAL = 50
    ERROR = 40
    WARNING = WARN = 30
    INFO = 20
    DEBUG = 10
    NOTSET = 0
    """

    # 로그 메시지를 기록한다.
    # 설정한 레벨 미만의 로그는 기록되지 않는다.
    logger.debug("debug 메시지입니다.")
    logger.info("info 메시지입니다.")
    logger.warning("warning 메시지입니다.")
    logger.error("error 메시지입니다.")
        
if __name__ == "__main__":
    log_level_test()
        