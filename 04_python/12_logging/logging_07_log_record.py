import logging
import time

# LogRecord를 직접 처리하는 커스텀 핸들러 정의
class CustomLogRecordHandler(logging.Handler):
    def emit(self, record):
        # LogRecord의 모든 속성을 반복하여 출력
        for attr, value in record.__dict__.items():
            if attr == 'created':
                readable_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(value))
                print(f"[{attr:<15}] : {value} (Readable: {readable_time})")
            else:
                print(f"[{attr:<15}] : {value}")
        if self.formatter:
            print(f"[Formatted Output]: {self.format(record)}")

def inspect_log_record():
    # 로거 인스턴스 생성 및 설정
    logger_name = "log_record_inspector"
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    # 커스텀 핸들러 인스턴스 및 포매터 생성 및 설정
    custom_handler = CustomLogRecordHandler()
    custom_formatter = logging.Formatter(
        fmt="[%(levelname)s][%(name)s:%(lineno)d] -> %(message)s",
        datefmt="%H:%M:%S"
    )
    custom_handler.setFormatter(custom_formatter)
    logger.addHandler(custom_handler)
    
    # 로깅 메시지 생성 (LogRecord 생성 유발)
    logger.warning("로깅 레코드의 모든 속성을 확인합니다.")
    logger.info(
        "커스텀 데이터 포함", 
        extra={"user_id": 42, "session_key": "abc123xyz"}
    )
    
if __name__ == "__main__":
    inspect_log_record()