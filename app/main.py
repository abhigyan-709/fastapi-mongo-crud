from fastapi import FastAPI, HTTPException
from app.schemas import ItemCreate, Item
from app import crud

app = FastAPI()

@app.post("/items/", response_model=Item)
def create(item: ItemCreate):
    item_id = crud.create_item(item.dict())
    return crud.get_item(item_id)

@app.get("/items/", response_model=list[Item])
def read_all():
    return crud.get_all_items()

@app.get("/items/{item_id}", response_model=Item)
def read_one(item_id: str):
    item = crud.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}", response_model=Item)
def update(item_id: str, item: ItemCreate):
    updated_item = crud.update_item(item_id, item.dict())
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@app.delete("/items/{item_id}")
def delete(item_id: str):
    success = crud.delete_item(item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item deleted"}
