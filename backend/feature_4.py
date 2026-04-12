```python
# models/todo.py
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4


class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None


class TodoInDB(BaseModel):
    id: UUID
    title: str
    description: Optional[str]

    class Config:
        orm_mode = True


# repositories/todo_repository.py
from typing import Optional
from uuid import UUID, uuid4
from models.todo import TodoInDB, TodoCreate

# In-memory store for example purpose.
# In real project, this would be replaced with actual DB access (e.g. SQLAlchemy)
class TodoRepository:
    def __init__(self):
        self._todos = {}

    def create(self, todo_create: TodoCreate) -> TodoInDB:
        todo_id = uuid4()
        todo_in_db = TodoInDB(
            id=todo_id,
            title=todo_create.title,
            description=todo_create.description,
        )
        self._todos[todo_id] = todo_in_db
        return todo_in_db

    def get(self, todo_id: UUID) -> Optional[TodoInDB]:
        return self._todos.get(todo_id)


# services/todo_service.py
from typing import Optional
from uuid import UUID
from models.todo import TodoCreate, TodoInDB
from repositories.todo_repository import TodoRepository


class TodoService:
    def __init__(self, repository: TodoRepository):
        self._repository = repository

    def create_todo(self, todo_create: TodoCreate) -> TodoInDB:
        return self._repository.create(todo_create)

    def get_todo(self, todo_id: UUID) -> Optional[TodoInDB]:
        return self._repository.get(todo_id)


# api/todo.py
from fastapi import APIRouter, Depends, HTTPException, status
from models.todo import TodoCreate, TodoInDB
from services.todo_service import TodoService
from repositories.todo_repository import TodoRepository

router = APIRouter()

# Dependency injection factory for repository & service
def get_todo_repository() -> TodoRepository:
    # In a real project, this might be a DB session-based repository instance
    # Here using a singleton in-memory repository for simplicity
    if not hasattr(get_todo_repository, "repo"):
        get_todo_repository.repo = TodoRepository()
    return get_todo_repository.repo


def get_todo_service(
    repository: TodoRepository = Depends(get_todo_repository),
) -> TodoService:
    return TodoService(repository)


@router.post("/todos", response_model=TodoInDB, status_code=status.HTTP_201_CREATED)
def create_todo(
    todo_create: TodoCreate,
    todo_service: TodoService = Depends(get_todo_service),
):
    todo = todo_service.create_todo(todo_create)
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Todo creation failed",
        )
    return todo


# main.py (for completeness, though not explicitly requested)
from fastapi import FastAPI
from api.todo import router as todo_router

app = FastAPI()
app.include_router(todo_router)
```