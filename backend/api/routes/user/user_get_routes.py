from fastapi import APIRouter, Depends, Request
from api.utils.logger import Logger
import api.middlewares.authentication_middleware as authentication_middleware
import api.repository.user_repo as user_repo
from fastapi.responses import JSONResponse
from api.schemas.user.request_schemas import user_request_schemas
from api.utils.exceptions import exceptions
from api.utils.nlp.youtube_transcript import get_transcript_v3
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

    @user.post('/get-youtube-transcript')
    async def get_youtube_transcript(
        request: user_request_schemas.GetYoutubeVideoTranscriptSchema
    ):
        print(request)
        try:
            text = get_transcript_v3(request.video_id)
    # text2=get_subtitles_test(video_id)
            if text:
                return {"transcript": text}
            else:
                return {"error": "No transcript available"}

        except Exception as e:
            Logger.error(e, log_msg="exception in get_user_profile route")
        
    @user.get('/{user_id}')
    async def get_user_profile(
        user_id: str
    ):
        try:
            response = await (
                user_repo.get_user_profile_handler(user_id)
            )

            return response

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



    return user


