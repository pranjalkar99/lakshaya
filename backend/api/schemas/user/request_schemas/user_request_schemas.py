from pydantic import AnyHttpUrl, BaseModel, EmailStr, root_validator, validator

class UserSearchSchema(BaseModel):
    text: str