from os import environ

import jwt
from fastapi import Request
from fastapi.responses import JSONResponse
# IMPORT FIREBASE
from api.config.firebase import firebase


def is_authenticated(request: Request):

    token = request.headers.get("Authorization", None)
    
    if token is not None:

        try:
            encoded_jwt = token.split(" ")[1]

            payload = jwt.decode(
                encoded_jwt, 
                environ.get("SECRET_KEY"), 
                algorithms=[environ.get("JWT_ALGORITHM")]
            )
            
            return {
                "flag": True, 
                "token": payload["token"], 
                "role": payload["role"]
            }
        
        except jwt.ExpiredSignatureError:

            return {"flag": False, "message": "token expired"}


    return {"flag": False, "message": "Authorization Header not present"}
