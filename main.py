import firebase_admin
from fastapi import FastAPI, Depends
from auth_system import login, registartion
from handlers import CRUD
from fastapi.middleware.cors import CORSMiddleware
from auth_system.base_auth import firebase_auth

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

@app.get("/secure_endpoint")
async def secure_endpoint(token: dict = Depends(firebase_auth)):
    user_id = token.get("user_id")
    email = token.get("email")

    return {"message": f"Hello, {email} (User ID: {user_id})! This is a secure endpoint."}
