```python
from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI(title="Clean Architecture FastAPI Server")
    # Add routers, middleware, events, etc. here

    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
```