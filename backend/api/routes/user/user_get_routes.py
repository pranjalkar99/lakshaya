from fastapi import APIRouter, Depends, Request
from api.utils.logger import Logger
import api.middlewares.authentication_middleware as authentication_middleware
import api.repository.user_repo as user_repo
from fastapi.responses import JSONResponse
from api.schemas.user.request_schemas import user_request_schemas
from api.utils.exceptions import exceptions
import requests

URL = "https://youtube.googleapis.com/youtube/v3/search"


async def test_function(roll_no, authorization):
    try:
        print(authorization["flag"])
        if authorization["flag"] == True:
            response = "it is working"
        else:
            response = "it is not working"

        return (response, authorization["flag"])

    except Exception as e:
        Logger.error(e, log_msg="exception in get_user_profile route")
        

def construct_router():

    user = APIRouter(
        tags=["User"]
    )

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

    return user
