from fastapi import APIRouter, Depends, Request
from api.utils.logger import Logger
from api.schemas.user.request_schemas import user_request_schemas

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

    @user.post('/{query}')
    async def get_search_results(
        query: str,
        ):

        try:
            response = await (
                
                
            )

            return response
        
        except Exception as e:
             Logger.error(e, log_msg="exception in get_user_profile route")
    
    return user