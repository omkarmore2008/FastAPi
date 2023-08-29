from typing import Union
from models import Item, Predeined


from typing_extensions import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/{item_id}")
def update_item(item: Item):
    return {"item_name": item.name, "item_id": item.price, "item_offer": item.is_offer}

@app.put("/items/{item_id}")
def update_item(item_id:int, item: Item):
    return {"item_name": item.name, "item_price": item.price, "item_offer": item.is_offer, "item_id": item_id}


@app.get("/users/me/{model_name1}")
def read_user_me(model_name1:str, model_name: Predeined):
    print(model_name1)
    print(Predeined.alexnet.value)
    print(model_name.value)
    return {"user_id": "the current user"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
