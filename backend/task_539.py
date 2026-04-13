```python
from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI(
        title="Clean Architecture FastAPI App",
        description="FastAPI application structured with clean architecture, repository pattern, and service layer",
        version="1.0.0"
    )

    # TODO: Include routers here as they are implemented
    # Example:
    # from your_app.api.v1 import api_router
    # app.include_router(api_router, prefix="/api/v1")

    return app

app = create_app()
```