from api.schemas.user.request_schemas import user_request_schemas
from api.models.user.user_model import UserModel
from api.utils.exceptions import exceptions

class User:
    """
        User database driver.
        Responsible for various student related
        tasks.
    """

    async def add_user(self, 
        user_details: user_request_schemas.UserSignupSchema
    ):
        try:
            user = UserModel(**user_details.__dict__)

            db_response = await UserModel.save(user)

            return True
        
        except Exception as e:
            print(f"{e} excep err : student driver")
            raise exceptions.UnexpectedError()
        
    
    