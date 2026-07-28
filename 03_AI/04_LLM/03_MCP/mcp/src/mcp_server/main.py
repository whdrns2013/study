from psycopg2.extras import RealDictCursor
from mcp.server.fastmcp import FastMCP
from core.settings import settings
from feature import search_email

mcp = FastMCP("AddressBook",
              host=settings.server.host,  # 호스트 주소
              port=settings.server.port,  # 포트 번호
)

@mcp.tool()
def search_email_by_name(name: str) -> str:
    return search_email.search_email_by_name(name)

@mcp.tool()
def search_email_by_group(group_name: str) -> str:
    return search_email.search_email_by_group(group_name)

def main():
    # mcp.run(transport="sse") # sse
    mcp.run() # openwebui

if __name__ == "__main__":
    main()
