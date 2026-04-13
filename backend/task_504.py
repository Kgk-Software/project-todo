```python
from fastapi import FastAPI

# Entity Layer (None needed here as this is a simple hello endpoint)

# Repository Layer (None needed since no data access)

# Service Layer
class HelloService:
    def say_hello(self) -> str:
        return "Hello, World!"

# API Layer
def create_app() -> FastAPI:
    app = FastAPI()
    hello_service = HelloService()

    @app.get("/hello")
    def hello():
        return {"message": hello_service.say_hello()}

    return app


app = create_app()
```