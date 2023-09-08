import requests, os, json
from common.models import UserDetails, CommonResponseModel
from common.temp_data import temp_data
from fastapi import status
from firebase_admin import auth


from fastapi import APIRouter

router = APIRouter()


@router.post("/login", tags=["authentication"])
async def login(user_credentials: UserDetails):
    '''
        User Login API
    '''
    API_KEY = os.environ.get("API_KEY", "AIzaSyBTXQeFwLauPrS5hKg_A2rrSLuEYuDt6PI")
    url = os.environ.get("LOGIN_URL", "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key")
    try:
        request_body = user_credentials.dict()
        
        if request_body:
            request_body.update({"returnSecureToken": True})
            request_body = json.dumps(request_body)
            print(request_body)
            response = requests.post(url=f"{url}={API_KEY}", data=request_body)
            response = response.json()
            print(response)

            if 'error' in response:
                return CommonResponseModel(status=status.HTTP_400_BAD_REQUEST, message=response["error"]["message"])

            return CommonResponseModel(status=status.HTTP_200_OK, message=response["idToken"])

        return CommonResponseModel(status=status.HTTP_400_BAD_REQUEST, message="Please enter details")

    except Exception as e:
        return CommonResponseModel(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e)
        )
