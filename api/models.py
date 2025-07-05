from pydantic import BaseModel
from datetime import date

class InventoryItem(BaseModel):
    product_id: str
    product_name: str
    category: str
    stock_quantity: int
    restock_threshold: int

class Sale(BaseModel):
    order_id: int
    product_id: str
    quantity_sold: int
    sale_date: date

class Review(BaseModel):
    review_id: int
    product_id: str
    product_name: str
    review_text: str
    rating: int
    review_date: date
