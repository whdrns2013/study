from core.settings import settings
from utils.db_manager import DBManager


def search_email_by_name(name: str) -> str:
    db = DBManager(db_type = settings.address_book.db_type,
                   db_conf = settings.address_book.db_conf)
    # query = f"SELECT email FROM {settings.address_book.table_name} WHERE name = '{name}'"
    make_query = lambda name:f"SELECT {settings.address_book.email_col}\
                               FROM {settings.address_book.table_name}\
                               WHERE {settings.address_book.name_col} = '{name}'"
    try:
        result = db.exec_query(make_query(name))
        if len(result) == 0:
            name = name.replace(' ', '')
            result = db.exec_query(make_query(name))
        return f"조회 결과: {result}" if result else f"name {name} 데이터 없음"
    except Exception as e:
        return f"Error: {str(e)}"

def search_email_by_group(group_name: str) -> str:
    db = DBManager(db_type = settings.address_book.db_type,
                   db_conf = settings.address_book.db_conf)
    make_query = lambda group_name:f"SELECT {settings.address_book.email_col}\
                                     FROM {settings.address_book.table_name}\
                                     WHERE {settings.address_book.group_name_col} = '{group_name}'"
    try:
        result = db.exec_query(make_query(group_name))
        if len(result) == 0:
            group_name = group_name.replace(' ', '')
            result = db.exec_query(make_query(group_name))
        return f"조회 결과: {result}" if result else f"name {group_name} 데이터 없음"
    except Exception as e:
        return f"Error: {str(e)}"