import logging

def about_formatter():
    
    # Logger 인스턴스 생성 및 설정
    logger_name = "about_formatter"
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # Handler 인스턴스들 생성
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level = logging.INFO)
    file_handler = logging.FileHandler(filename="logs/formatter_log.log", mode="a", encoding="utf-8")
    file_handler.setLevel(logging.ERROR)
    
    # Formatter 생성
    stream_formatter = logging.Formatter(
        fmt="[%(levelname)s] %(asctime)s - %(message)s",
        datefmt="%Y-%m-%d"
    )
    file_formatter = logging.Formatter(
        fmt="[%(levelname)s] %(asctime)s [%(pathname)s] line %(lineno)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    # Handler 에 Formatter 할당
    stream_handler.setFormatter(stream_formatter)
    file_handler.setFormatter(file_formatter)
    
    # Logger 에 Handler 할당
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    
    # 로그 레코드 생성 및 핸들러에 전달
    logger.info("debug message")
    logger.error("error message")
    
    
if __name__ == "__main__":
    about_formatter()