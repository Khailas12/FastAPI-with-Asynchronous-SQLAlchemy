from fastapi import FastAPI
from services.api import router as item_router

app = FastAPI()

app.include_router(item_router, tags=["Items"], prefix='/items')

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}