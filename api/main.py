from fastapi import FastAPI
from api.models import InventoryItem, Sale, Review
from api.crud import get_inventory, get_sales, get_reviews

app = FastAPI()

@app.get("/inventory", response_model=list[InventoryItem])
def read_inventory():
    return get_inventory()

@app.get("/sales", response_model=list[Sale])
def read_sales():
    return get_sales()

@app.get("/reviews", response_model=list[Review])
def read_reviews():
    return get_reviews()
