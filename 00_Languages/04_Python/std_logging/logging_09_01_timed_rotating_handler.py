import logging
from logging.handlers import TimedRotatingFileHandler
import time
from typing import Literal

LOG_LEVEL_TYPE = Literal["DEBUG", "INFO", "WARNING", "ERROR"]
LOG_WHEN = Literal["S", "M", "H", "D", "midnight", "W{0}", "W{1}", "W{2}", "W{3}", "W{4}", "W{5}", "W{6}"]

def timed_rotating_logging():
    
    # timed rotating file handler
    # 위치 : logging.handlers.TimedRotatingFileHandler
    # 로그를 특정 시간 간격이나 날짜 변화에 따라 자동으로 새 파일로 전환(롤오버)해준다.
    
    logger_name = "timed_rotating_file_handler_logger"
    logger = logging.getLogger(logger_name)
    
    handler = TimedRotatingFileHandler(
        filename = "rotating_logs/timed_rotating",   # 파일이름, 이름 뒤에 날짜가 붙게 된다.
        when = "S",                         # 롤오버가 발생하는 주기 (midnight, h, d s ..)
        interval = 10,                      # when 주기의 간격 10 + when(s) = 10초마다
        backupCount = 10,                   # 보관할 백업 파일의 최대 개수 (e.g.최대 10개만 보관)
        encoding = "utf-8",                 # 파일 인코딩
        delay = True,                       # 핸들러가 실제로 로그를 기록하기 전까지 파일 열기를 지연 (첫 로그 발생 시 파일 생성)
        utc = False,                        # 현지 시간으로 계산할지, UTC로 계산할지 (True / False)
        atTime = None,                      # when='midnight' 또는 when='d'일 때, 정확히 몇 시에 롤오버를 수행할지 지정.
        errors = "이건 뭐지"                  # 파일 인코딩/디코딩 오류 발생 시 오류 처리 방식을 지정 (string)
    )
    
    formatter = logging.Formatter(
        fmt = "%(asctime)s %(name)s %(message)s"
    )
    
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    for i in range(10):
        logger.warning(f"{i} :: 반복적인 메시지입니다.")
        time.sleep(3)
        
if __name__ == "__main__":
    timed_rotating_logging()