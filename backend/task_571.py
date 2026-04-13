```python
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

# Entity layer: For this simple use case no specific entity is needed

# Repository layer: No data access needed for this simple example

# Service layer: Encapsulates business logic
class HelloWorldService:
    def get_greeting(self) -> str:
        return "Hello World"

# API layer: FastAPI app and endpoints
def create_app() -> FastAPI:
    app = FastAPI()
    service = HelloWorldService()

    @app.get("/", response_class=PlainTextResponse)
    def read_root():
        return service.get_greeting()

    return app

app = create_app()
```