import uuid

def generate_chat_id() -> str:
    return str(uuid.uuid4())