workers = 4
worker_class = "uvicorn.workers.UvicornWorker"
timeout = 30

port = 18080
bind = f'0.0.0.0:{port}'
reload = True