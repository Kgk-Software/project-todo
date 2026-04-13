```python
from fastapi import FastAPI
from app.api.v1.hello import router as hello_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="Clean Architecture FastAPI Application",
        description="API built with FastAPI following clean architecture principles",
        version="1.0.0",
    )

    # Include API routers (versioned)
    app.include_router(hello_router, prefix="/api/v1")

    return app

app = create_app()
```