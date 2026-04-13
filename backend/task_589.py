```python
from fastapi import APIRouter, Depends
from app.core.responses import create_response

router = APIRouter()


@router.get("/hello")
async def hello():
    """
    GET /hello endpoint handler that returns a greeting message with consistent response logic.
    """
    return create_response(data={"message": "Hello, world!"}, message="Greeting delivered successfully.")
```
