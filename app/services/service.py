from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from services.schema import ItemUpdateSchema
from services.models import Item



async def create_item(db: AsyncSession, name: str, description: str):
    new_item = Item(name=name, description=description)
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)
    return new_item


async def get_item(db: AsyncSession, item_id: int):
    result = await db.execute(select(Item).filter(Item.id == item_id))
    item = result.scalars().first() 
    return item


async def update_item(db: AsyncSession, item_id: int, item_data: ItemUpdateSchema):
    item = await get_item(db, item_id)
    
    if not item:
        return None  
    
    if item_data.name:
        item.name = item_data.name
    if item_data.description:
        item.description = item_data.description
    
    await db.commit()
    await db.refresh(item)
    return item

async def delete_item(db: AsyncSession, item_id: int):
    item = await get_item(db, item_id)
    
    if not item:
        return None  
    await db.delete(item)
    await db.commit()    
    return item