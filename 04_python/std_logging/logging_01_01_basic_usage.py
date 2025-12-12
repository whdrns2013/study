import logging  # logging 표준 라이브러리를 사용한다.

def logging_basic():
    
    # 로거 객체를 생성
    logger_name = "logging_basic"             # 로거 이름 설정
    logger = logging.getLogger(logger_name)

    # 로깅 설정
    filename = "logs/logging_basic_log.log"    # 로그를 기록할 파일 경로 설정
    logging.basicConfig(        
        filename=filename,      # 로그를 기록할 파일 경로
        level=logging.DEBUG,    # 로거가 처리할 최소 로그 레벨
        encoding='utf-8'        # 파일 인코딩
        )
        # basicConfig : 간단한 기본 로깅 설정
        # filename 을 지정하면 FileHandler 로 파일에 로그를 기록하며,
        # filename 을 지정하지 않으면 StreamHandler 로 콘솔에 로그를 출력한다.

    # 로그 메시지를 기록한다.
    logger.info("info 메시지입니다.")
    logger.debug("debug 메시지입니다.")
    logger.warning("warning 메시지입니다.")
    logger.error("error 메시지입니다.")
    
if __name__ == "__main__":
    logging_basic()