from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()


class Item(BaseModel):
    name:str
    price:int
    tax:float | None=None
    
@app.get("/items")
async def all_items(skip:int=0,limit:int=10):
    dummy_data=[
        {"name":"lap1", "price":100},
        {"name":"lap2", "price":200, "tax":10.10},
        {"name":"lap3", "price":300, "tax":20.20},
        {"name":"lap4", "price":400, "tax":30.30},
        {"name":"lap5", "price":500, "tax":40.40},
        {"name":"lap6", "price":600, "tax":50.50},
        {"name":"lap7", "price":700, "tax":60.60},
        {"name":"lap8", "price":800, "tax":70.70},
        {"name":"lap9", "price":900, "tax":80.80},
        {"name":"lap10", "price":1000, "tax":90.90}
    ]
    dummy_data= dummy_data[skip:skip+limit]
