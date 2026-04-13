```python
from fastapi import FastAPI, Depends
from pydantic import BaseModel


# Domain Entity
class Hello:
    def __init__(self, message: str):
        self.message = message


# Service Layer
class HelloService:
    def get_message(self) -> Hello:
        return Hello(message="Hello, World!")


# Response DTO
class HelloResponseDTO(BaseModel):
    message: str


# Dependency provider for service
def get_hello_service() -> HelloService:
    return HelloService()


# FastAPI app instance
app = FastAPI()


@app.get("/hello", response_model=HelloResponseDTO)
async def hello(service: HelloService = Depends(get_hello_service)):
    hello_entity = service.get_message()
    return HelloResponseDTO(message=hello_entity.message)
```