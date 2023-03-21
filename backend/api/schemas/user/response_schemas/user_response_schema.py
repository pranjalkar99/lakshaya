from pydantic import AnyHttpUrl, BaseModel, EmailStr, root_validator, validator
from typing import Optional
from api.models.user.user_model import *
class UserSearchResponseSchema(BaseModel):
    text: str

class UserDataSchema(BaseModel):
    user_id: str
    fname: str
    lname: str
    standard: int
    email: EmailStr
    tests: Optional[List[ExamModel]] = []
    # branch: Optional[str] = None
    # gender: str
    # phone: Optional[str] = None