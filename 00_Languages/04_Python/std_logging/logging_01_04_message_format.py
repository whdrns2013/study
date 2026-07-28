import logging  # logging 표준 라이브러리를 사용한다.

def change_message_format():
    # 로거 객체를 생성
    logger_name = "message_format"
    logger = logging.getLogger(logger_name)

    # 로깅 설정
    filename = "logs/message_format_log.log"
    logging.basicConfig(filename=filename, level=logging.INFO, encoding='utf-8')

    # 기본적인(basicConfig) 메시지 포맷 테스트
    logger.error("기본적인(basicConfig) 메시지 포맷 테스트")
    
    # 포맷 변경
    # 자세한 포맷 작성법은 logging.__init__.py 의 Formatter 클래스 부분에서 확인 가능
    logger.propagate = False # 전파 방지
    logger.handlers.clear()
    new_format = logging.Formatter("%(lineno)s %(levelname)s - %(process)s %(filename)s %(message)s") # 새로운 포맷
    file_handler = logging.FileHandler(filename=filename, mode='a', encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(new_format) # 포맷 설정
    logger.addHandler(file_handler)
    logger.error("로깅 포맷 설정을 바꿔보았습니다.")
    
if __name__ == "__main__":
    change_message_format()