

```python
# main.py
from fastapi import FastAPI
from app.api.v1.routers import routers as v1_routers

app = FastAPI()

app.include_router(v1_routers, prefix="/api/v1")
```

```bash
fastapi dev main.py
fastapi dev --port=8080 --host=0.0.0.0 main.py
```
