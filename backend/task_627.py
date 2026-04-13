```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers from your API layer
# from your_project.api import some_router

def create_app() -> FastAPI:
    """
    Application factory function that creates and configures the FastAPI app instance.
    Following Clean Architecture principles, setup middleware, routers, and other app-level settings here.
    """
    app = FastAPI(title="Your Project API", version="1.0.0")

    # Example Cors middleware setup - adjust origins as necessary
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Change to allowed origins in production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Register API routers here, separating endpoint definitions (adhering to Clean Architecture)
    # app.include_router(some_router, prefix="/some-path", tags=["SomeTag"])

    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    # Run the app with uvicorn, typically externalized to a config or env variables
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
```