import logging  # logging 표준 라이브러리를 사용한다.

class DefatultClass:
    def change_message_format():
        # 기본적인 사용법
        logger_name = "change_message_format"             # 로거 이름 설정
        filename = "log/change_message_format_log.log"    # 로그를 기록할 파일 경로 설정

        # 로거 객체를 생성
        logger = logging.getLogger(logger_name)

        # 로깅 설정 (전역, 1회만)
        logging.basicConfig(filename=filename,
                            level=logging.INFO,
                            encoding='utf-8',
                            format="커스텀 포맷 테스트 - %(levelname)s:%(message)s") # 메시지의 포맷을 결정

        # 로그 메시지를 기록한다.
        logger.info("info 메시지입니다.")
        logger.debug("debug 메시지입니다.")
        logger.warning("warning 메시지입니다.")
        logger.error("error 메시지입니다.")
        
        # 로그 포맷은 아래와 같은 항목들을 사용할 수 있다.
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
        
        # 로깅 포맷 설정을 바꾼다면
        new_format = logging.Formatter("%(lineno)s %(levelname)s - %(process)s %(filename)s %(message)s")
        file_handler = logging.FileHandler(
            filename=filename,
            mode='a',
            encoding='utf-8',
        )
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(new_format)
        if logger.handlers:
            logger.handlers = [] # 중복 쓰기 방지를 위해 핸들러 비움
        logger.addHandler(file_handler)
        logger.error("로깅 포맷 설정을 바꿔보았습니다.")