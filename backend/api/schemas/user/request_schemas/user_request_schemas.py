from pydantic import AnyHttpUrl, BaseModel, EmailStr, root_validator, validator
from typing import Optional
from api.models.user.user_model import *

class UserSearchSchema(BaseModel):
    query: str
    max_results: int

class UserSignupSchema(BaseModel):
    user_id: str
    fname: str
    lname: str
    standard: int
    branch: Optional[str] = ""
    gender: str
    email: EmailStr
    phone: Optional[str]

class UserTextSummarySchema(BaseModel):
    transcript: str

class GetYoutubeVideoTranscriptSchema(BaseModel):
    video_id: str

class UserUpdateData(BaseModel):
    fname: Optional[str]
    lname: Optional[str]
    standard: Optional[int]
    branch: Optional[str] = ""
    gender: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[str]
    tests: Optional[List[ExamModel]] = []