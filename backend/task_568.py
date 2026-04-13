```python
from fastapi import FastAPI, Response
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

    @app.get("/hello")
    def hello():
        content = service.get_hello_greeting()
        return Response(content=content, media_type="text/plain")

    return app

app = create_app()
```