FROM python:3.11-slim

ARG SHARED_DIR_MOUNT_POINT_ARG=/shared_dir/
ENV SHARED_DIR_MOUNT_POINT=${SHARED_DIR_MOUNT_POINT_ARG}

WORKDIR /app
RUN pip install uv
COPY . .
RUN uv sync
RUN chmod +x /app/core/train.sh
CMD ["/app/core/train.sh"]