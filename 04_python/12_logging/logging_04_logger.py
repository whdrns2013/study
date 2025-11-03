import logging

def about_logger():
    
    # 로거 인스턴스를 생성
    # getLogger 는 이름이 제공되면 해당 이름을 가진 로거 인스턴스를 반환한다.
    # 그렇지 않으면 루트 인스턴스를 반환한다.
    # 서로 다른 이름의 로거는 각기 다른 메모리 주소를 가진다.
    logger_name = "about_logger"
    logger = logging.getLogger(logger_name)
    
    # setLevel
    # 로거가 처리할 가장 낮은 심각도의 로그 레벨을 지정
    # 로그 레벨은 logging.INFO 처럼 쓰거나, 로그 레벨에 해당하는 정수값을 넣어도 된다. (아래 둘은 동일)
    logger.setLevel(logging.INFO)
    logger.setLevel(20)
    
    # addHandler
    # 핸들러를 로거에 할당한다.
    # Hnadler에 대해서는 Handler 소개 글에서 자세히 다루겠다.
    handler = logging.StreamHandler()
    handler.setLevel(level = logging.INFO)
    formatter = logging.Formatter()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    # 로그 레코드 생성 및 핸들러에 전달
    # debug(), info(), error().. 등의 메서드를 통해 로그 레코드를 생성하고, 핸들러에 전달한다.  
    # 각각의 메서드는 자신의 이름과 동일한 레벨의 로그 레벨을 가진 로그 레코드를 만들게 된다.  
    # 예를 들어, debug() 메서드는 logging.DEBUG 레벨의 로그 레코드를 만든다.  
    logger.debug("debug message")
    logger.error("error message")
    
    # logger 이름에 따른 인스턴스 생성
    # logger 인스턴스는 "이름"에 따라 생성되며 관리된다.
    # 이름이 다르면 서로 다른 로거 인스턴스이다.
    # 서로 다른 인스턴스는 당연히 서로 다른 메모리 주소를 갖는다.
    print(f"{logger_name} 로거의 id : {id(logger)}")
    new_logger_name = "new_logger"
    logger = logging.getLogger("new_logger")
    print(f"{new_logger_name} 로거의 id : {id(logger)}")
    logger = logging.getLogger(logger_name)
    print(f"다시 돌아온 {logger_name} 로거의 id : {id(logger)}")
    
if __name__ == "__main__":
    about_logger()