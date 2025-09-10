FROM python:3.11-slim

WORKDIR /app
RUN pip install uv
COPY . .
RUN uv sync
RUN chmod +x /app/core/train.sh
CMD ["/app/core/train.sh"]