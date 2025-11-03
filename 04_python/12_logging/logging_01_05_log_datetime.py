import logging  # logging 표준 라이브러리를 사용한다.
import time

def log_datetime():
    # 로거 객체를 생성
    logger_name = "datetime_format"
    logger = logging.getLogger(logger_name)

    # 로깅 설정
    filename = "logs/datetime_format_log.log"
    logging.basicConfig(filename=filename, level=logging.INFO, encoding='utf-8',
                        format="%(asctime)s - %(message)s")

    # 기본적인 시간 표현
    logger.info("기본적인 datetime format 입니다.")
    
    # 시간 표현 방법 변경
    logger.propagate = False
    new_format = logging.Formatter(fmt="%(asctime)s - %(message)s",
                                   datefmt="%Y년 %m월 %d일 %H시 %M분 %S초") # 새로운 포맷
    file_handler = logging.FileHandler(filename=filename, mode='a', encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(new_format) # 포맷 설정
    logger.addHandler(file_handler)
    logger.error("변경된 datetime format 입니다.")
    
if __name__ == "__main__":
    log_datetime()