from pydantic import AnyHttpUrl, BaseModel, EmailStr, root_validator, validator
from typing import Optional

class UserSearchSchema(BaseModel):
    query: str
    max_results: int

class UserSignupSchema(BaseModel):
    user_id: str
    fname: str
    lname: str
    standard: int
    branch: Optional[str]
    gender: str
    email: EmailStr
    phone: Optional[str]