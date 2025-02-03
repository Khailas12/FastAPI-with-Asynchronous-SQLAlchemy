from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    name: str
    description: str

    class Config:
        from_attributes = True


class ItemUpdateSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

    class Config:
        from_attributes = True
