import logging
import os
# Lib/logging/__init__.py

logger_name = '.'.join(os.path.normpath(__file__).replace('\\', '/').split('/')[-2:])
filename = "test_log.log"
level = logging.INFO

logger = logging.getLogger(logger_name)
logging.basicConfig(filename=filename, level=level, encoding='utf-8')

# 로그 메시지를 기록한다. 설정한 level 미만의 로그는 기록되지 않는다.
logger.info("info 메시지입니다.")
logger.debug("debug 메시지입니다.")
logger.warning("warning 메시지입니다.")
logger.error("error 메시지입니다.")

# logger를 여러 번 호출해도 같은 객체를 반환한다.  
print(id(logger))
logger = logging.getLogger(logger_name)
print(id(logger))

# 로거의 이름이 바뀌면 새로운 로거 객체가 생성됩니다.
new_logger_name = "new_logger"
logger = logging.getLogger(new_logger_name)
logger.debug("새로운 logger 입니다.")
print(id(logger))

# 다시 처음 로거의 이름으로 가져오면 원래의 로거 객체가 반환됩니다.
# 즉, 로거 객체는 "이름"으로 각각의 로거 객체로 정의되며
# 프로그래밍에서는 여러 로거를 선언해서 쓸 수 있고, 중복된 이름의 로거를 만들지 않도록 주의해야 합니다.
logger = logging.getLogger(logger_name)
print(id(logger))

def main():
    pass

if __name__ == "__main__":
    main()
