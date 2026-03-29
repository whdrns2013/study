from abc import ABC, abstractmethod
import psycopg2
from psycopg2.extras import RealDictCursor

class DB(ABC):
    @abstractmethod
    def connect(self, config:dict) -> None:
        pass
    @abstractmethod
    def exec_query(self, query:str):
        pass
    @abstractmethod
    def close(self) -> None:
        pass
    
    
class PostgresDB(DB):
    def __init__(self):
        self.conn = None
        
    def connect(self, config:dict) -> None:
        try:
            self.conn = psycopg2.connect(**config)
        except Exception as e:
            raise ConnectionError(f"DB Connection failed: {e}")
    def exec_query(self, query:str):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query)
            return cur.fetchall()
    def close(self):
        if self.conn:
            self.conn.close()


class DBManager:
    
    DB_MAP = {
        "postgres":PostgresDB
    }
    
    def __init__(self, db_type:str, db_conf:dict):
        if db_type not in self.DB_MAP:
            raise ValueError(f"Unsupported DB type :: {db_type}")
        self.db = self.DB_MAP[db_type]()
        self.db_conf = db_conf
        
    def exec_query(self, query:str):
        self.db.connect(self.db_conf)
        result = self.db.exec_query(query)
        self.db.close()
        return result
    
        