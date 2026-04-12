```python
# Design Artifacts and Documentation for Backend Service 
# Framework: FastAPI
# Architecture: Clean Architecture with Repository Pattern and Service Layer

"""
1. Overview
-----------
This backend service demonstrates a clean architecture implementation using FastAPI. 
It includes separation of concerns with domain, repository, service, and API layers.
The repository pattern is used to abstract data access (in this example, in-memory).
Business logic is encapsulated inside the service layer.

2. Package Structure
--------------------
app/
├── domain/
│   ├── models.py           # Domain entities / models
│   └── exceptions.py       # Custom domain exceptions
│
├── repositories/
│   ├── repository.py       # Repository interface
│   └── in_memory_repo.py   # In-memory repository implementation
│
├── services/
│   └── item_service.py     # Business logic service layer
│
├── api/
│   └── v1/
│       └── endpoints.py    # FastAPI endpoints / controllers
│
├── main.py                 # FastAPI app setup and startup
└── config.py               # Configuration settings

3. Design Explanation
---------------------

- Domain Layer:
  Contains models representing the core business entities and domain exceptions.

- Repository Layer:
  Defines repository interfaces and concrete implementations.
  Provides abstraction over persistence/storage mechanisms.

- Service Layer:
  Implements business rules and coordinates between repositories and API layers.
  Responsible for transactions, validations, and other business logic.

- API Layer:
  FastAPI controllers that depend only on services, exposing HTTP endpoints.

This architecture allows easy swapping of repository implementations
(e.g., from in-memory to database) without changing higher layers.

4. Example Code Sections (All included below)
----------------------------------------------

- Domain model: Item (id, name, description)
- Repository interface: ItemRepository
- In-memory repository: InMemoryItemRepository
- Service layer: ItemService
- FastAPI endpoints: CRUD for items

"""

# app/domain/models.py
from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

# app/domain/exceptions.py
class ItemNotFoundException(Exception):
    pass


# app/repositories/repository.py
from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.models import Item


class ItemRepository(ABC):

    @abstractmethod
    def get_by_id(self, item_id: int) -> Optional[Item]:
        pass

    @abstractmethod
    def list(self) -> List[Item]:
        pass

    @abstractmethod
    def add(self, item: Item) -> Item:
        pass

    @abstractmethod
    def update(self, item: Item) -> Item:
        pass

    @abstractmethod
    def delete(self, item_id: int) -> None:
        pass


# app/repositories/in_memory_repo.py
from typing import Dict, List, Optional
from app.domain.models import Item
from app.repositories.repository import ItemRepository
from app.domain.exceptions import ItemNotFoundException


class InMemoryItemRepository(ItemRepository):
    def __init__(self):
        self._items: Dict[int, Item] = {}

    def get_by_id(self, item_id: int) -> Optional[Item]:
        return self._items.get(item_id)

    def list(self) -> List[Item]:
        return list(self._items.values())

    def add(self, item: Item) -> Item:
        if item.id in self._items:
            raise ValueError(f"Item with id {item.id} already exists.")
        self._items[item.id] = item
        return item

    def update(self, item: Item) -> Item:
        if item.id not in self._items:
            raise ItemNotFoundException(f"Item with id {item.id} not found.")
        self._items[item.id] = item
        return item

    def delete(self, item_id: int) -> None:
        if item_id not in self._items:
            raise ItemNotFoundException(f"Item with id {item_id} not found.")
        del self._items[item_id]


# app/services/item_service.py
from typing import List
from app.repositories.repository import ItemRepository
from app.domain.models import Item
from app.domain.exceptions import ItemNotFoundException


class ItemService:
    def __init__(self, repository: ItemRepository):
        self._repository = repository

    def get_item(self, item_id: int) -> Item:
        item = self._repository.get_by_id(item_id)
        if not item:
            raise ItemNotFoundException(f"Item with id {item_id} not found.")
        return item

    def list_items(self) -> List[Item]:
        return self._repository.list()

    def create_item(self, item: Item) -> Item:
        # Potential business rules & validations could go here
        return self._repository.add(item)

    def update_item(self, item: Item) -> Item:
        existing = self._repository.get_by_id(item.id)
        if not existing:
            raise ItemNotFoundException(f"Item with id {item.id} not found.")
        # business logic validation could go here
        return self._repository.update(item)

    def delete_item(self, item_id: int) -> None:
        self._repository.delete(item_id)


# app/api/v1/endpoints.py
from fastapi import APIRouter, HTTPException, status
from typing import List
from app.domain.models import Item
from app.services.item_service.py import ItemService
from app.domain.exceptions import ItemNotFoundException

router = APIRouter()


# Dependency Injection of service is simplified here for example.
# In production, use proper DI tools or FastAPI Depends.
item_service = None  # placeholder, to be initialized


@router.get("/items", response_model=List[Item])
async def list_items():
    return item_service.list_items()


@router.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    try:
        return item_service.get_item(item_id)
    except ItemNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    try:
        return item_service.create_item(item)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    if item_id != item.id:
        raise HTTPException(status_code=400, detail="Item ID in path and body must match")
    try:
        return item_service.update_item(item)
    except ItemNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):
    try:
        item_service.delete_item(item_id)
    except ItemNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))


# app/main.py
from fastapi import FastAPI
from app.api.v1.endpoints import router as item_router
from app.repositories.in_memory_repo import InMemoryItemRepository
from app.services.item_service import ItemService

app = FastAPI(title="Clean Architecture FastAPI Example")

# Initialize repository and service
repository = InMemoryItemRepository()
service = ItemService(repository)

# Inject repository/service
import app.api.v1.endpoints as endpoints
endpoints.item_service = service  # Simple dependency injection

app.include_router(item_router, prefix="/api/v1", tags=["items"])


# For manual testing run:
# uvicorn app.main:app --reload


"""
Summary
- The code above fully implements a backend in FastAPI following clean architecture principles.
- The repository pattern abstracts data storage behind an interface.
- The service layer encapsulates business logic and communicates only with the repository.
- The API layer uses FastAPI endpoints to expose the service layer.
- This separation facilitates maintainability, testing, and scalability.
"""
```