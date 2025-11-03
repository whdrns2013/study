import logging  # logging 표준 라이브러리를 사용한다.
from logging.handlers import TimedRotatingFileHandler
import time

class DefatultClass:
    def timed_rotating_logging():
        
        # timed rotating file handler
        # : logging.handlers.TimedRotatingFileHandler
        # 로그를 특정 시간 간격이나 날짜 변화에 따라 자동으로 새 파일로 전환(롤오버)해준다.
        
        logger_name = "timed_rotating_file_handler_logger"
        logger = logging.getLogger(logger_name)
        
        handler = TimedRotatingFileHandler(
            # filename, 파일이름, 이름 뒤에 날짜가 붙게 된다.
            filename = "log/timed_rotating_file_handler_log.log",
            # when : 롤오버가 발생하는 주기 (midnight, h, d .. 뭐가 있는지 더 보기)
            when = "s",
            # interval : when 주기의 간격 30 + when(s) = 30초마다
            interval = 10,
            # backupCount : 보관할 백업 파일의 최대 개수 (최대 3개만 보관)
            backupCount = 100,
            # encoding : 파일 인코딩
            encoding = "utf-8",
            # delay : True / False 이거 찾아보기
            delay = True,
            # utc : 현지 시간으로 계산할지, UTC로 계산할지 (True / False)
            utc = False,
            # atTime : when='midnight' 또는 when='d'일 때, 정확히 몇 시에 롤오버를 수행할지 지정.
            atTime = None,
            # errors : 파일 인코딩/디코딩 오류 발생 시 오류 처리 방식을 지정 (string)
            errors = "이건 뭐지"
        )
        
        formatter = logging.Formatter(
            fmt = "%(asctime)s %(name)s %(message)s"
        )
        
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        for i in range(10):
            logger.warning(f"{i} :: 반복적인 메시지입니다.")
            time.sleep(5)
            
        
        # 이렇게 하면, 현재 작성되는 파일은 "timed_rotating_file_handler_log.log" 에 쌓이며,
        # 지정한 interval이 지나면, 과거의 로그는 날짜를 붙여서 저장한다. e.g. timed_rotating_file_handler_log.log.2025-11-03_11-14-02
        # 즉, 날짜가 안붙은 건 현재 인터벌의 파일임
        
