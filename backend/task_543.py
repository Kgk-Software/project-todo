```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(
    title="Clean Architecture FastAPI App",
    description="FastAPI application structured with clean architecture, repository pattern, and service layer",
    version="1.0.0"
)

class ResponseModel(BaseModel):
    success: bool
    data: dict | None = None
    message: str | None = None

def create_response(
    *,
    success: bool,
    data: dict | None = None,
    message: str | None = None,
    status_code: int = 200
) -> JSONResponse:
    """
    Constructs a standardized JSON response with given parameters.
    """
    payload = ResponseModel(success=success, data=data, message=message).dict(exclude_none=True)
    return JSONResponse(content=payload, status_code=status_code)

@app.get("/health", response_model=ResponseModel)
async def health_check():
    """
    Basic health check endpoint illustrating response logic.
    """
    data = {"status": "ok"}
    return create_response(success=True, data=data, message="Service is healthy")

@app.get("/example", response_model=ResponseModel)
async def example_endpoint():
    """
    Example endpoint returning some data using the response logic.
    """
    example_data = {"foo": "bar", "count": 123}
    return create_response(success=True, data=example_data)
```