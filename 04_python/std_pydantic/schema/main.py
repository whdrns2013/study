from schemas.schemas import LogSenderSchema
from datetime import datetime

def main():
    # e.g content
    system_name = "model_train"
    date_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    message = "the test log message"
    
    # make send body
    body = LogSenderSchema(
        system = system_name,
        date_time = date_time,
        message = message
    )
    
    # when you send
    send_body = body.model_dump()   # pydantic 2.0 이상
    print(f"send_body (model_dump) : {send_body}")
    send_body = body.dict()         # pydantic 2.0 미만
    print(f"send_body (dict) : {send_body}")


if __name__ == "__main__":
    main()
