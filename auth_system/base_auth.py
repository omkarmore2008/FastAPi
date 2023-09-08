from typing import Optional

from fastapi import Depends, HTTPException, Query
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from firebase_admin import auth


async def firebase_auth(
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False)),
    token: Optional[str] = Query(None, include_in_schema=False),
):
    try:
        if credentials is None:
            if token is None:
                raise HTTPException(status_code=401, detail="Unauthorized")
            else:
                credentials = HTTPAuthorizationCredentials(
                    scheme="Bearer", credentials=token
                )

            return auth.verify_id_token(credentials.credentials if credentials else token)
    except Exception as e:
        raise HTTPException(status_code=401, detail="Unauthorized")
