```python
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from abc import ABC, abstractmethod

# Repository Layer
class GreetingRepository(ABC):
    @abstractmethod
    def fetch_greeting(self) -> str:
        pass

class GreetingRepositoryImpl(GreetingRepository):
    def fetch_greeting(self) -> str:
        return "Hello World"

# Service Layer
class GreetingService:
    def __init__(self, repository: GreetingRepository):
        self._repository = repository

    def get_hello_greeting(self) -> str:
        return self._repository.fetch_greeting()

# API Layer
def create_app() -> FastAPI:
    app = FastAPI()
    repository = GreetingRepositoryImpl()
    service = GreetingService(repository)

    @app.get("/hello", response_class=PlainTextResponse)
    def hello():
        return service.get_hello_greeting()

    return app

app = create_app()
```