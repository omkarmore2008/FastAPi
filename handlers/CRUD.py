from common.temp_data import temp_data
from common.models import RequestModel, CommonResponseModel
from fastapi import APIRouter, status, Depends
from auth_system.base_auth import firebase_auth
from google.cloud import firestore

db = firestore.AsyncClient()

router = APIRouter()

"""
@router.get("/add-data", tags=["Data Crud Operations"])
'''
    API to add temporary data to database
'''
async def add_data():
    try:
        for data in temp_data:
            await db.collection("car_data").add(data)
        return {"message": "Data Added successfully"}
    except Exception as e:
        return {"message": str(e)}
"""


@router.post("/add-data", tags=["Data Crud Operations"])
async def add_data(request: RequestModel, token: dict = Depends(firebase_auth)):
    '''
        API to add data into database
    '''
    try:
        request_body = request.dict()
        if request_body:
            await db.collection("car_data").add(request_body)
            return CommonResponseModel(
                status=status.HTTP_201_CREATED,
                message="Data added successfully"
            )

        return CommonResponseModel(
            status=status.HTTP_400_BAD_REQUEST,
            message="Please enter data"
        )

    except Exception as e:
        return CommonResponseModel(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e)
        )
