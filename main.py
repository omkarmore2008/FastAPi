import firebase_admin
from fastapi import FastAPI
from auth_system import login, registartion
from handlers import CRUD
from fastapi.middleware.cors import CORSMiddleware


origins = ["*"]
firebase_admin.initialize_app()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["default"])
def root():
    return {"Hello": "World"}


app.include_router(registartion.router)
app.include_router(login.router)

app.include_router(CRUD.router)
