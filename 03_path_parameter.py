#input in url by user
@app.get("/items/{item_name}")
async def get_items(item_name:str,Company: str|None=None):
    return{"item_name":item_name,"Company":Company}
