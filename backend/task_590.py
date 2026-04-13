```python
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Any, Dict

app = FastAPI(title="Clean Architecture API with Response Logic")


class ResponseModel(BaseModel):
    success: bool
    data: Any = None
    message: str = ""


def create_response(
    *,
    data: Any = None,
    message: str = "",
    success: bool = True,
    status_code: int = status.HTTP_200_OK,
) -> JSONResponse:
    """
    Standard JSON response wrapper to ensure consistent API responses.
    """
    payload = ResponseModel(success=success, data=data, message=message).dict()
    return JSONResponse(content=payload, status_code=status_code)


@app.get("/health", response_model=ResponseModel)
async def health_check():
    """
    Simple health check endpoint demonstrating consistent response format.
    """
    return create_response(data={"status": "ok"}, message="Service is healthy.")


@app.get("/items/{item_id}", response_model=ResponseModel)
async def get_item(item_id: int):
    """
    Sample endpoint to demonstrate response logic and error handling.
    """
    fake_db = {1: {"name": "Item One"}, 2: {"name": "Item Two"}}

    item = fake_db.get(item_id)
    if not item:
        return create_response(
            data=None,
            message=f"Item with id {item_id} not found.",
            success=False,
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return create_response(data=item, message="Item retrieved successfully.")


@app.post("/items/", response_model=ResponseModel, status_code=status.HTTP_201_CREATED)
async def create_item(item: Dict[str, Any]):
    """
    Sample create item endpoint with response logic.
    """
    # Here would be business logic to create and save the item
    created_item = item  # Stub for demonstration
    return create_response(
        data=created_item,
        message="Item created successfully.",
        success=True,
        status_code=status.HTTP_201_CREATED,
    )
```