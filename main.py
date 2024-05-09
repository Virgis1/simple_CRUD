from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

db = {}

class Item(BaseModel):
    name: str
    description: str = None
    price: float


@app.post("/items/")
def create_item(item: Item):
    item_dict = item.dict()
    db[item.name] = item_dict
    return item_dict

@app.get("/items/{name}")
def read_item(name: str):
    if name not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return db[name]

@app.put("/items/{name}")
def update_item(name: str, item: Item):
    if name not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    db[name] = item.dict()
    return db[name]

@app.delete("/items/{name}")
def delete_item(name: str):
    if name not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    del db[name]
    return {"message": "Item deleted successfully"}

@app.get("/items/")
def get_all_items():
    return db

