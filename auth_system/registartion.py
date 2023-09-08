from common.models import UserDetails, CommonResponseModel
from fastapi import status
from firebase_admin import auth
# from firebase_admin import credentials


from fastapi import APIRouter

router = APIRouter()

@router.post("/register", tags=["authentication"])
async def register(user_credentials: UserDetails):
    '''
        User Registration API
    '''
    try:
        email = user_credentials.email.strip()
        password = user_credentials.password.strip()

        if not email or not password:
            return CommonResponseModel(
                status=status.HTTP_400_BAD_REQUEST,
                message="Please provide email and password"
            )

        if password and len(password) < 8:
            return CommonResponseModel(
                status=status.HTTP_400_BAD_REQUEST,
                message="Password is too weak"
            )

        user_id = auth.create_user(email=email, password=password)
        return CommonResponseModel(
            status=status.HTTP_201_CREATED,
            message=f"Registration Successful with uid: {user_id.uid}"
        )

    except Exception as e:
        return CommonResponseModel(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e)
        )
