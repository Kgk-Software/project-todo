```python
from fastapi import FastAPI, Response, status
from abc import ABC, abstractmethod

# Repository Layer
class GreetingRepository(ABC):
    @abstractmethod
    def fetch_greeting(self) -> str:
        pass

class GreetingRepositoryImpl(GreetingRepository):
    def fetch_greeting(self) -> str:
        # Return greeting or None if not found (simulated)
        return "Hello World"

# Service Layer
class GreetingService:
    def __init__(self, repository: GreetingRepository):
        self._repository = repository

    def get_hello_greeting(self) -> str | None:
        return self._repository.fetch_greeting()

# API Layer
def create_app() -> FastAPI:
    app = FastAPI()
    repository = GreetingRepositoryImpl()
    service = GreetingService(repository)

    @app.get("/hello")
    def hello():
        greeting = service.get_hello_greeting()
        if greeting is not None:
            return Response(content=greeting, media_type="text/plain", status_code=status.HTTP_200_OK)
        else:
            return Response(content="Greeting not found", media_type="text/plain", status_code=status.HTTP_404_NOT_FOUND)

    return app

app = create_app()
```