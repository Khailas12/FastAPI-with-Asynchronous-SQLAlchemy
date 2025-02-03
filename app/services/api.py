from utils import dependency
from services.schema import ItemBase, ItemUpdateSchema
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from services import service  


router = APIRouter()


@router.post("/")
async def add_item(name: str, description: str, db: AsyncSession = Depends(dependency.get_db)):
    item = await service.create_item(db, name, description)
    return {"message": "Item created", "item_id": item.id}


@router.get("/{item_id}", response_model=ItemBase)
async def get_item(item_id: int, db: AsyncSession = Depends(dependency.get_db)):
    item = await service.get_item(db, item_id)

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item  


@router.put("/{item_id}")
async def update_item(
    item_id: int,
    item_data: ItemUpdateSchema, 
    db: AsyncSession = Depends(dependency.get_db),
):
    item = await service.update_item(db, item_id, item_data)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"message": "Item updated", "item_id": item.id}


@router.delete("/{item_id}")
async def delete_item(
    item_id: int, 
    db: AsyncSession = Depends(dependency.get_db),
):
    deleted_item = await service.delete_item(db, item_id)
    
    if deleted_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted", "item_id": item_id}