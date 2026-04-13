```python
from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI(
        title="My Clean Architecture FastAPI Application",
        description="API built with FastAPI following clean architecture principles",
        version="1.0.0"
    )
    return app


app = create_app()
```