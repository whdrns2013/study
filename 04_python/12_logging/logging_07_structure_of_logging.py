import logging


class DefatultClass:
    # Logger
    def about_logger():
        logger_name = "about_logger"             # 로거 이름 설정
        filename = "log/about_logger_log.log"    # 로그를 기록할 파일 경로 설정
        
        # 로거 객체를 생성
        # getLogger 는 이름이 제공되면 해당 이름을 가진 로거 인스턴스를 반환한다.
        # 그렇지 않으면 루트 인스턴스를 반환한다.
        # 서로 다른 이름의 로거는 각기 다른 메모리 주소를 가진다.
        logger = logging.getLogger(logger_name)
        
        # logger 이름이 달라지면 다른 인스턴스가 생성된다.
        # 따라서 당연하게 다른 메모리 주소를 갖는다.
        print(id(logger))
        logger = logging.getLogger("new_logger")
        print(id(logger))
        logger = logging.getLogger(logger_name)
        print(id(logger))
        
        # setLevel : 로거가 처리할 가장 낮은 심각도의 로그 레벨을 지정
        # input 값은 정수형 (logging.INFO 와 같이 사용해도 된다.)
        logger.setLevel(20) # logging.INFO
        
        # Hnadler : 자세한 핸들러에 대한 내용은 아래 Handler 부분에서 다룬다.
        handler = logging.StreamHandler()
        handler.setLevel(level = logging.INFO)
        
        # Formatter : 자세한 포매터에 대한 내용은 아래 Formatter 부분에서 다룬다.
        formatter = logging.Formatter()
        handler.setFormatter
        
        # logger.debug(), logger.info() ...
        # 이들은 로그 메시지를 만들고, 이에 해당하는 수준의 로그 레코드를 만든다.
        logger.debug("something")
        """
        # 예시 : Logger.debug()
        def debug(self, msg, *args, **kwargs):
            if self.isEnabledFor(DEBUG):
                self._log(DEBUG, msg, args, **kwargs)
        # 아래는 logger.debug, logger.info 의 실제 실행을 맡는 _log 메서드
        def _log(self, level, msg, args, exc_info=None, extra=None, stack_info=False,
             stacklevel=1):
        sinfo = None
        if _srcfile:
            #IronPython doesn't track Python frames, so findCaller raises an
            #exception on some versions of IronPython. We trap it here so that
            #IronPython can use logging.
            try:
                fn, lno, func, sinfo = self.findCaller(stack_info, stacklevel)
            except ValueError: # pragma: no cover
                fn, lno, func = "(unknown file)", 0, "(unknown function)"
        else: # pragma: no cover
            fn, lno, func = "(unknown file)", 0, "(unknown function)"
        if exc_info:
            if isinstance(exc_info, BaseException):
                exc_info = (type(exc_info), exc_info, exc_info.__traceback__)
            elif not isinstance(exc_info, tuple):
                exc_info = sys.exc_info()
        record = self.makeRecord(self.name, level, fn, lno, msg, args,
                                 exc_info, func, extra, sinfo)
        self.handle(record)
        """
        
        # logger.exception()
        # logger.error() 와 비슷한 로그를 생성하며, 스택 트레이스를 덤프한다.
        
        
        # logger.log()
        # 로그 수준을 명시하여 로깅을 수행한다.


        # logger 는 부모- 자식 과 같은 계층적 구조를 이룰 수 있다.
        # 예를 들어, 이름이 foo 인 로거가 주어지면, foo.bar, foo.bar.baz, 그리고 foo.bam 의 이름을 가진 로거는 모두 foo 의 자손
        # 로거의 propagate 어트리뷰트를 False로 설정하면 전파가 중지됨


    # Handler
    def about_handler():
        # Handler는 적절한 로그 메시지를 처리기의 지정된 대상으로 전달하는 역할
        # e.g. 1번 핸들러 : 모든 로그 메시지를 로그 파일로 보낸다.
        # e.g. 2번 핸들러 : 에러 수준 이상의 모든 로그 메시지를 표준 출력으로 보낸다.
        # e.g. 3번 핸들러 : 사용자 정의의 심각한 수준 이상의 모든 로그 메시지를 이메일로 보낸다.
        # -> 이 경우 3개의 핸들러가 필요하다.
        # 즉, 핸들러는 "로그 메시지를 어딘가에 보내는" 역할을 하는 객체이다.
        logger_name = "about_handler_logger"
        logger = logging.getLogger(logger_name)
        
        # Handler의 종류는
        # Handler : 
        # StreamHandler : Handler 를 상속한 핸들러.
        # FileHandler : StreamHandler 를 상속한 핸들러.
        # NullHandler : Handler 를 상속한 핸들러.
        # _StderrHandler : StreamHandler 를 상속한 핸들러. # -> 히든 클래스
        # file_handler 는 다른 핸들러들과 다르게 추가적인 설정이 필요하다. (초기화할 때 제공해야 함)
        
        # handler = logging.Handler() # 추상화된 인터페이스. 바로 사용할 수는 없다.
        stream_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(
                                            filename="log/about_handler_log.log",
                                            encoding="utf-8",
                                            mode = "a"
                                          )
        null_handler = logging.NullHandler()
        
        # 그러면 커스텀 동작을 하는 핸들러도 만들 수 있을 것이다.
        class CustomHandler(logging.Handler):
            def __init__(self):
                super().__init__()
            def debug(self):
                if self.level <= logging.DEBUG:
                    self._log()
            def info(self):
                if self.level <= logging.INFO:
                    self._log()
            def warning(self):
                if self.level <= logging.WARNING:
                    self._log()
            def error(self):
                if self.level <= logging.ERROR:
                    self._log()
            def emit(self, record):
                try:
                    print(f"CustomHandler {logging.getLevelName(self.level)} : something ran!")
                except RecursionError:  # See issue 36272
                    raise
        custom_handler = CustomHandler()

        # Handler 의 어트리뷰트 1. setLevel()
        # setLevel() : 로거와 비슷하게, 핸들러가 처리할 가장 낮은 심각도를 지정한다.
        # 따라서 일차적으로 로거가 이 로그가 자신이 처리할 심각도인지 확인한 뒤
        # 핸들러 또한 자신이 처리할 심각도인지 확인한다.
        # e.g. DEBUG 레벨의 로거에 INFO 레벨의 파일핸들러, ERROR 레벨의 이메일핸들러가 있다고 하자
        # WARNING 레벨의 로그가 발생하면, 로거와 파일핸들러는 이를 처리하고, 이메일핸들러는 처리하지 않는다.

        stream_handler.setLevel(logging.INFO)
        file_handler.setLevel(logging.WARNING)
        custom_handler.setLevel(level=logging.ERROR)
        
        # Handler 의 어트리뷰트 2. setFormatter()
        # setFormatter() 는 처리기가 사용할 포매터를 지정한다.
        # Formatter는 아래에서 더 자세히 알아보겠지만, 로그 메시지 포맷을 지정한다.
        
        stream_formatter = logging.Formatter(fmt="stream handler : %(message)s")
        file_formatter = logging.Formatter(fmt="file handler : %(message)s")
        custom_formatter = logging.Formatter(fmt="custom handler : %(message)s")
        
        stream_handler.setFormatter(stream_formatter)
        file_handler.setFormatter(file_formatter)
        custom_handler.setFormatter(custom_formatter)

        # Handler 의 어트리뷰트 3. addFilter, removeFilter
        # Filter 는 이건 좀 나중에 해보자.

        # Handler 를 logger 에 추가할 때에는 Logger.addHandler() 메서드를 사용한다.
        # 또한 다수개의 핸들러를 한 번에 추가할 수도 있다? -> 없다. append라.
        """
        def addHandler(self, hdlr):
        with _lock:
            if not (hdlr in self.handlers):
                self.handlers.append(hdlr)
        """
        handler_list = [stream_handler, file_handler, custom_handler]
        for handler in handler_list:
            logger.addHandler(handler)

        # 테스트
        # 이제 로그레벨에 따른 로깅을 수행해본다.
        logger.info("info 메시지입니다.")
        logger.debug("debug 메시지입니다.")
        logger.warning("warning 메시지입니다.")
        logger.error("error 메시지입니다.")

    # Formatter
    def about_handler():
        # Formatter 는 어떤 로그 메시지를 특정 패턴과 함께 나태내게 하는 포맷(형식)을 정하는 것
        # 포맷은 문자 또는 문자열, 그리고 logging 라이브러리에서 제공하는 몇 가지 패턴을 사용할 수 있다.
        formatter = logging.Formatter(
            fmt = "%(levelname)s %(asctime)s %(name)s %(pathname)s %(message)s", # 포맷 지정 (패턴 이용)
            datefmt = "%Y-%m-%d %H:%M", # 날짜 형식 지정
            style = "%" # '%', '{' 또는 '$' 중 하나입니다. 이 중 하나가 지정되지 않으면, '%' 가 사용됨. 만약 $를 쓰면 $(name)s 를 대체해서 쓰는 듯?
        )
        
        """
        %(name)s            Name of the logger (logging channel)
        %(levelno)s         Numeric logging level for the message (DEBUG, INFO,
                            WARNING, ERROR, CRITICAL)
        %(levelname)s       Text logging level for the message ("DEBUG", "INFO",
                            "WARNING", "ERROR", "CRITICAL")
        %(pathname)s        Full pathname of the source file where the logging
                            call was issued (if available)
        %(filename)s        Filename portion of pathname
        %(module)s          Module (name portion of filename)
        %(lineno)d          Source line number where the logging call was issued
                            (if available)
        %(funcName)s        Function name
        %(created)f         Time when the LogRecord was created (time.time_ns() / 1e9
                            return value)
        %(asctime)s         Textual time when the LogRecord was created
        %(msecs)d           Millisecond portion of the creation time
        %(relativeCreated)d Time in milliseconds when the LogRecord was created,
                            relative to the time the logging module was loaded
                            (typically at application startup time)
        %(thread)d          Thread ID (if available)
        %(threadName)s      Thread name (if available)
        %(taskName)s        Task name (if available)
        %(process)d         Process ID (if available)
        %(processName)s     Process name (if available)
        %(message)s         The result of record.getMessage(), computed just as
                            the record is emitted
        """
        
        logger_name = "about_handler_logger"
        logger = logging.getLogger(logger_name)
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        
        # 만든 formatter는 아래와 같이 핸들러에 세팅한다.
        handler.setFormatter(formatter)



## LogRecord
# https://docs.python.org/ko/3/howto/logging.html#configuring-logging 여기서부터


## Filter