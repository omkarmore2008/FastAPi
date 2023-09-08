import firebase_admin, os
from typing import Union
from models import Item, Predeined, UserDetails, CommonResponseModel
from google.cloud import firestore
from typing_extensions import Annotated
from fastapi import Depends, FastAPI, status
from fastapi.security import OAuth2PasswordBearer
from firebase_admin import auth, credentials


creds_details = os.environ.get("creds", {})
creds = credentials.Certificate("serviceTokenKey.json")
firebase_admin.initialize_app(creds)
app = FastAPI()
db = firestore.AsyncClient()


@app.get("/", tags=["default"])
def read_root():
    return {"Hello": "World"}


@app.post("/register", tags=["authentication"])
async def register(user_credentials: UserDetails):
    '''
        User Registration API
    '''
    try:
        email = user_credentials.email.strip()
        password = user_credentials.password.strip()

        if not email or not password:
            return CommonResponseModel(
                status=str(status.HTTP_400_BAD_REQUEST),
                message="Please provide email and password"
            )

        if password and len(password) < 8:
            return CommonResponseModel(
                status=str(status.HTTP_400_BAD_REQUEST),
                message="Password is too weak"
            )

        user_id = auth.create_user(email=email, password=password)
        return CommonResponseModel(
            status=str(status.HTTP_201_CREATED),
            message=f"Registration Successful with uid: {user_id.uid}"
        )

    except Exception as e:
        return CommonResponseModel(
            status=str(status.HTTP_500_INTERNAL_SERVER_ERROR),
            message=str(e)
        )


@app.post("/login", tags=["authentication"])
async def login(user_credentials: UserDetails):
    '''
        User Login API
    '''
    try:
        email = user_credentials.email.strip()
        password = user_credentials.password.strip()

        if not email or not password:
            return CommonResponseModel(
                status=str(status.HTTP_400_BAD_REQUEST),
                message="Please provide email and password"
            )

        user = auth.get_user_by_email(email)
        uid = user.uid
        claims = {
            "email": email
        }

        login_data = auth.create_custom_token(uid, claims)
        return CommonResponseModel(
            status=str(status.HTTP_201_CREATED),
            message=f"Login Successful"
        )

    except Exception as e:
        return CommonResponseModel(
            status=str(status.HTTP_500_INTERNAL_SERVER_ERROR),
            message=str(e)
        )
