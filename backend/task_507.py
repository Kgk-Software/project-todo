```python
from fastapi import FastAPI, Depends
from pydantic import BaseModel


# Define Response Model
class HelloResponse(BaseModel):
    message: str


# Service Layer
class HelloService:
    def say_hello(self) -> str:
        # Business logic - in this simple case just return greeting string
        return "Hello, World!"


# Dependency Injection Provider for Service Layer
def get_hello_service() -> HelloService:
    return HelloService()


# API Layer with response logic, using Pydantic model for response serialization
def create_app() -> FastAPI:
    app = FastAPI(title="Clean Architecture FastAPI Server with Response Logic")

    @app.get("/hello", response_model=HelloResponse)
    def hello(hello_service: HelloService = Depends(get_hello_service)):
        message = hello_service.say_hello()
        return HelloResponse(message=message)

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
```