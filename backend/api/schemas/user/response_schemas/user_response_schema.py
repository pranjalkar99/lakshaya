from pydantic import AnyHttpUrl, BaseModel, EmailStr, root_validator, validator

class UserSearchResponseSchema(BaseModel):
    text: str