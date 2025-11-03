import logging  # logging 표준 라이브러리를 사용한다.

class DefatultClass:
    def logging_to_file():
        # 기본적인 사용법
        logger_name = __name__                      # 로거 이름을 파일 이름으로 자동 설정
                                                    # 로거 이름은 기본적으로 로그 메시지의 두 번째에 들어감
        filename = "log/logging_to_file_log.log"    # 로그를 저장할 파일 결정

        # 로거 객체를 생성
        logger = logging.getLogger(logger_name)

        # 로깅 설정
        logging.basicConfig(filename=filename,
                            level=logging.INFO,
                            encoding='utf-8')

        # 로그 메시지를 기록한다.
        logger.info("file에 로깅하는 첫 메시지입니다.")
        
        # -------------- 아래는 고급 사용법 -------------- #
        
        # 로깅 설정을 "쓰기"로 다시 열면 -> 로그파일이 새로 써짐
        file_handler = logging.FileHandler(
            filename=filename,
            mode='w',
            encoding='utf-8'
        )
        file_handler.setLevel(logging.INFO)
        logger.addHandler(file_handler) # 파일 핸들러를 추가하면 추가적으로 로깅이 됨. 즉, 여러 파일에 한 번에 동일한 내용을 로깅할 수 있음
        logger.error("새로운 편집 메시지입니다.")
        
        # 로깅 설정을 "추가"로 바꾼다면 -> 로그파일에 추가되어 써짐 (기본값)
        file_handler = logging.FileHandler(
            filename=filename,
            mode='a',
            encoding='utf-8'
        )
        file_handler.setLevel(logging.INFO)
        if logger.handlers:
            logger.handlers = [] # 중복 쓰기 방지를 위해 핸들러 비움
        logger.addHandler(file_handler)
        logger.error("추가 편집 메시지입니다.")
        
        # 로깅 설정을 "읽기"로 바꾼다면
        file_handler = logging.FileHandler(
            filename=filename,
            mode='r',
            encoding='utf-8'
        )
        file_handler.setLevel(logging.INFO)
        logger.addHandler(file_handler)
        # logger.error("읽기 전용 메시지입니다.") # 에러 발생 : io.UnsupportedOperation: not writable
        