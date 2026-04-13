```python
from fastapi import FastAPI, Depends
from pydantic import BaseModel

# Response Model
class HelloResponse(BaseModel):
    message: str

# Service Layer
class HelloService:
    def say_hello(self) -> str:
        return "Hello, World!"

# Dependency Injection
def get_hello_service() -> HelloService:
    return HelloService()

# FastAPI app factory
def create_app() -> FastAPI:
    app = FastAPI(title="Clean Architecture FastAPI")

    @app.get("/hello", response_model=HelloResponse)
    def hello(hello_service: HelloService = Depends(get_hello_service)):
        greeting = hello_service.say_hello()
        return HelloResponse(message=greeting)

    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
```