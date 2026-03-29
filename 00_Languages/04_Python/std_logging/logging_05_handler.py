import logging

def about_handler():
    
    # Logger 인스턴스 생성 및 설정
    logger_name = "about_handler"
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # StreamHandler 인스턴스 생성
    stream_handler = logging.StreamHandler()        # 핸들러의 종류를 정할 수 있다.
    stream_handler.setLevel(level = logging.INFO)   # 핸들러가 처리할 최소 로그 레벨을 설정한다.
    formatter = logging.Formatter()                 # Formatter 생성 : 추후에 다룸
    stream_handler.setFormatter(formatter)          # Formatter 할당
    
    # FileHandler 인스턴스 생성
    file_handler = logging.FileHandler(
        filename="logs/handler_log.log",
        mode="a",
        encoding="utf-8"
    )
    file_handler.setLevel(logging.ERROR)            # 핸들러마다 각기 다른 로그 레벨을 설정할 수 있다.
    new_formatter = logging.Formatter()             # Formatter 생성 : 추후에 다룸
    file_handler.setFormatter(new_formatter)        # 핸들러마다 각기 다른 포매터를 설정할 수 있다.
    
    # addHandler : Logger 에 Handler 할당
    # 하나의 Logger 에 다수 개의 Handler 를 할당할 수 있다.
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    
    # 로그 레코드 생성 및 핸들러에 전달
    logger.info("debug message")
    logger.error("error message")
    
    
if __name__ == "__main__":
    about_handler()