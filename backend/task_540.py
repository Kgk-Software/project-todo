```python
from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI(
        title="My Clean Architecture FastAPI Application",
        description="An example FastAPI app following clean architecture principles",
        version="1.0.0"
    )

    # Here you can include router registrations, middleware, event handlers, etc.
    # For example:
    # from your_project.api import router as api_router
    # app.include_router(api_router)

    return app

app = create_app()
```