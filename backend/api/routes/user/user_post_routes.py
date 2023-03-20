from fastapi import APIRouter, Depends, Request
from api.utils.logger import Logger
from api.schemas.user.request_schemas import user_request_schemas
import requests
from api.drivers.user import user_drivers
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi import APIRouter, Depends, HTTPException, Request, status
from summarizer import Summarizer
from api.repository import user_repo

URL = "https://youtube.googleapis.com/youtube/v3/search"

def construct_router():
    user = APIRouter(
            tags=["User"]
        )
    
    @user.post('/')
    async def get_text(
        request: user_request_schemas.UserSearchSchema,
        ):

        try:
            response = await (
                
                
            )

            return response
        
        except Exception as e:
             Logger.error(e, log_msg="exception in get_user_profile route")

    @user.post('/signup')
    async def signup(
        request: user_request_schemas.UserSignupSchema,
        ):

        try:
            user = user_drivers.User()

            response = await user.add_user(request)

            message = "User added successfully"

            return JSONResponse(
                status_code=status.HTTP_201_CREATED, 
                content=message
            )
        
        except Exception as e:
             Logger.error(e, log_msg="exception in get_user_profile route")

    @user.post('/search')
    async def get_search_results(
        request: user_request_schemas.UserSearchSchema,
    ):

        try:
            params = {
                "part": "snippet",
                "maxResults": request.max_results,
                "q": request.query,
                "key" : "AIzaSyBA5cXWRn7vWcCFtvCC2SfcTg_3-GCsxB4"
            }
            response = requests.get(url=URL, params=params)

            return response.json()

        except Exception as e:
            Logger.error(e, log_msg="exception in get_user_profile route")

    @user.post('/analyze-text')
    async def analyze_text(
        request: user_request_schemas.UserTextSummarySchema,
    ):
        # print(request.transcript)
        try:
            response = await (
                user_repo.analyze_text(request)
            )

            print(response)

            return response

            return response
        except Exception as e:
            Logger.error(e, log_msg="exception in get_user_profile route")

    
    return user