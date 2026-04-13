```python
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from abc import ABC, abstractmethod


# Entities (Domain Models)
class Item:
    def __init__(self, id: int, name: str, description: Optional[str]):
        self.id = id
        self.name = name
        self.description = description


# DTOs (Data Transfer Objects)
class ItemCreateDTO(BaseModel):
    name: str
    description: Optional[str] = None


class ItemResponseDTO(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


# Repository Interface
class ItemRepositoryInterface(ABC):
    @abstractmethod
    async def get_item(self, item_id: int) -> Optional[Item]:
        pass

    @abstractmethod
    async def list_items(self) -> List[Item]:
        pass

    @abstractmethod
    async def create_item(self, item: Item) -> Item:
        pass


# In-memory Repository Implementation (for demonstration/testing)
class InMemoryItemRepository(ItemRepositoryInterface):
    def __init__(self):
        self._items = []
        self._next_id = 1

    async def get_item(self, item_id: int) -> Optional[Item]:
        for item in self._items:
            if item.id == item_id:
                return item
        return None

    async def list_items(self) -> List[Item]:
        return self._items.copy()

    async def create_item(self, item: Item) -> Item:
        item.id = self._next_id
        self._next_id += 1
        self._items.append(item)
        return item


# Service Layer
class ItemService:
    def __init__(self, repository: ItemRepositoryInterface):
        self._repository = repository

    async def get_item(self, item_id: int) -> Item:
        item = await self._repository.get_item(item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    async def list_items(self) -> List[Item]:
        return await self._repository.list_items()

    async def create_item(self, item_create_dto: ItemCreateDTO) -> Item:
        new_item = Item(id=0, name=item_create_dto.name, description=item_create_dto.description)
        created_item = await self._repository.create_item(new_item)
        return created_item


# Dependency Injection
def get_repository() -> ItemRepositoryInterface:
    # Normally this might return a db repository, here for demo an in-memory repo
    return InMemoryItemRepository()


def get_service(
    repository: ItemRepositoryInterface = Depends(get_repository),
) -> ItemService:
    return ItemService(repository)


# FastAPI app and API layer
app = FastAPI()


@app.post("/items/", response_model=ItemResponseDTO, status_code=201)
async def create_item(
    item_create: ItemCreateDTO,
    service: ItemService = Depends(get_service),
):
    created_item = await service.create_item(item_create)
    return ItemResponseDTO(
        id=created_item.id,
        name=created_item.name,
        description=created_item.description,
    )


@app.get("/items/{item_id}", response_model=ItemResponseDTO)
async def get_item(
    item_id: int,
    service: ItemService = Depends(get_service),
):
    item = await service.get_item(item_id)
    return ItemResponseDTO(
        id=item.id,
        name=item.name,
        description=item.description,
    )


@app.get("/items/", response_model=List[ItemResponseDTO])
async def list_items(
    service: ItemService = Depends(get_service),
):
    items = await service.list_items()
    return [
        ItemResponseDTO(id=item.id, name=item.name, description=item.description) for item in items
    ]
```