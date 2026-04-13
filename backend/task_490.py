```python
from fastapi import FastAPI
from pydantic import BaseModel

# Entity (Domain Model)
class HelloMessage:
    def __init__(self, message: str):
        self.message = message


# Service Layer
class HelloService:
    def get_hello_message(self) -> HelloMessage:
        return HelloMessage(message="Hello, World!")


# Response DTO
class HelloResponseDTO(BaseModel):
    message: str


# Dependency Injection function for service
def get_hello_service() -> HelloService:
    return HelloService()


# FastAPI app instance
app = FastAPI()


@app.get("/hello", response_model=HelloResponseDTO)
async def hello_endpoint(service: HelloService = Depends(get_hello_service)):
    hello_message = service.get_hello_message()
    return HelloResponseDTO(message=hello_message.message)


# Import Depends from fastapi
from fastapi import Depends
```