```python
from fastapi import FastAPI, Depends

# Service Layer
class HelloService:
    def say_hello(self) -> str:
        return "Hello, World!"

# Dependency Injector
def get_hello_service() -> HelloService:
    return HelloService()

def create_app() -> FastAPI:
    app = FastAPI(title="Clean Architecture FastAPI Server with Dependency Injection")

    @app.get("/hello")
    def hello(hello_service: HelloService = Depends(get_hello_service)):
        return {"message": hello_service.say_hello()}

    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
```