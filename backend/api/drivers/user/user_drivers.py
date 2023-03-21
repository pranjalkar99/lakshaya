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
        

    async def get_user_profile(self, user_id):
        #TODO: add suitable doc string and exception handling
        user = await UserModel.find_one(
            UserModel.user_id == user_id
        )

        print(user)

        if user is None:
            return False       

        return user.__dict__
        