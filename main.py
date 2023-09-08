import firebase_admin
from fastapi import FastAPI
from auth_system import login, registartion
from handlers import CRUD
# creds_details = os.environ.get("creds", {})
# creds = credentials.Certificate("serviceTokenKey.json")


firebase_admin.initialize_app()
app = FastAPI()


@app.get("/", tags=["default"])
def root():
    return {"Hello": "World"}


app.include_router(registartion.router)
app.include_router(login.router)

app.include_router(CRUD.router)
