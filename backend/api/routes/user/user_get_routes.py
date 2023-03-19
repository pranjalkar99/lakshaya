from fastapi import APIRouter, Depends, Request
from api.utils.logger import Logger

def construct_router():
    
        user = APIRouter(
            tags=["User"]
        )
    
        @user.get('/{roll_no}')
        async def get_user_profile(
            roll_no: str,
            # authorization = Depends(authentication_middleware.is_authenticated)
            ):
    
            try:
                response = await (
                    # student_repo.get_student_profile_handler(roll_no, authorization)
                    
                )
    
                return response
            
            except Exception as e:
                 Logger.error(e, log_msg="exception in get_user_profile route")
    
    
        return user