```bash
# git clone
git clone ~
# 컨테이너 환경설정
vi .env_template
mv .env_template .env
# MCP Server 환경설정
vi src/core/config.ini.template
mv src/core/config.ini.template src/core/config.ini
# docker compose up
sudo docker compose up -d
```