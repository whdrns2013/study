import logging  # logging 표준 라이브러리를 사용한다.

def logging_to_file():
    
    # 로거 객체를 생성
    logger_name = "log_to_file"
    logger = logging.getLogger(logger_name)
    logger.propagate = False # 전파 방지

    # 로깅 설정
    filename = "logs/log_to_file_log.log"
    logging.basicConfig(filename=filename,
                        level=logging.INFO,
                        encoding='utf-8')

    """
    파일에 로그를 작성할 때에는 "편집 모드" 를 지정할 수 있다.
    편집모드는 w(쓰기), a(추가), r(읽기) 세 가지가 있다.
    """
    
    # 기본 편집 모드는 a(추가) 이다.
    logger.info("file에 로깅하는 첫 메시지입니다.")
    logger.info("file에 로깅하는 두 번째 메시지입니다.")
    with open(filename, 'r') as f:
        print(f.readlines())
    
    # 편집 모드를 w(쓰기)로 하면 -> 이전의 내용이 없어지고, 새로 쓰여진다.
    logger.handlers.clear()
    file_handler = logging.FileHandler(filename=filename, mode='w',encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.error("w(쓰기 모드)로 로깅한 새로운 로그입니다.")
    with open(filename, 'r') as f:
        print(f.readlines())
    
    # 편집 모드를 a(추가)로 바꾼다면 -> 이전의 내용에 이어서 로그가 작성된다.
    logger.handlers.clear()
    file_handler = logging.FileHandler(filename=filename, mode='a',encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.error("a(추가 모드)로 로깅한 추가 편집 메시지입니다.")
    with open(filename, 'r') as f:
        print(f.readlines())
    
    # 로깅 설정을 "읽기"로 바꾼다면
    logger.handlers.clear()
    file_handler = logging.FileHandler(filename=filename, mode='r', encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.error("읽기 전용 메시지입니다.") # 에러 발생 : io.UnsupportedOperation: not writable

if __name__ == "__main__":
    logging_to_file()