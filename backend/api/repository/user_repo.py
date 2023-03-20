import json
from api.utils.exceptions import exceptions
from fastapi.responses import JSONResponse
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def is_authenticated_and_authorized(request, authorization):

    # Check if user is authenticated and authorized
    if not authorization["flag"]:
        raise exceptions.AuthenticationError()
    
    if authorization["token"] != request["student_id"]:
        raise exceptions.UnauthorizedUser(authorization["token"])
    
async def get_info(request, authorization):
    try:
        if type(request) == dict:
            is_authenticated_and_authorized(request, authorization)
        else:
            is_authenticated_and_authorized(request.__dict__, authorization)
        
        # Executes student instance method
        # response = await fn(request)
        response = "it is definiteky working"
        
        if response:
            return JSONResponse(status_code=200, 
            content={"message" : "student information updated"})
        
        return JSONResponse(status_code=200, 
            content={"message" : "student information cannot be updated"})
    
    except exceptions.AuthenticationError as e:
        
            return JSONResponse(status_code=403, 
                content={"message" : authorization["message"]})
    

async def get_search_results(request):
    try:
        response = await (
            user_repo.get_search_results(request)
        )
        
        return response
    
    except Exception as e:
        Logger.error(e, log_msg="exception in get_user_profile route")
    
