```python
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

# Entity layer: No specific entities needed for this simple example

# Repository layer: No data access needed but we implement an interface for demonstration and future extension
from abc import ABC, abstractmethod

class GreetingRepository(ABC):
    @abstractmethod
    def fetch_greeting(self) -> str:
        pass

class GreetingRepositoryImpl(GreetingRepository):
    def fetch_greeting(self) -> str:
        # In real app this might fetch from DB or config
        return "Hello World"

# Service layer: Handles business logic and coordinates with repository
class GreetingService:
    def __init__(self, repository: GreetingRepository):
        self._repository = repository

    def get_hello_greeting(self) -> str:
        return self._repository.fetch_greeting()

# API layer: FastAPI app and endpoints
def create_app() -> FastAPI:
    app = FastAPI()
    repository = GreetingRepositoryImpl()
    service = GreetingService(repository)

    @app.get("/hello", response_class=PlainTextResponse)
    def hello_endpoint():
        return service.get_hello_greeting()

    return app

app = create_app()
```