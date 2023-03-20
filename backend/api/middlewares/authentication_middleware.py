from os import environ

import jwt
from fastapi import Request
from fastapi.responses import JSONResponse
# IMPORT FIREBASE
import firebase_admin
from firebase_admin import credentials


def is_authenticated(request: Request):

    token = request.headers.get("Authorization", None)
    
    if token is not None:

        try:
            encoded_jwt = token.split(" ")[1]

            # verify id token
            decoded_token = firebase_admin.auth.verify_id_token(encoded_jwt)
            uid = decoded_token['uid']
            print(uid)
            
            return {
                "flag": True, 
                "uid": payload["uid"], 

            }
        
        except jwt.ExpiredSignatureError:

            return {"flag": False, "message": "token expired"}


    return {"flag": False, "message": "Authorization Header not present"}
