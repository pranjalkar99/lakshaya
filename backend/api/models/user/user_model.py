from beanie import Document, Indexed
from typing import Any, Dict, List, Optional
import datetime

class ExamModel(Document):
    question: str
    answer: str
    options: List[str]
    marks: int
    evaluation: bool

class TestSeriesModel(Document):
    score: int
    test_id: str
    

class UserModel(Document):
    register_date: datetime.datetime = datetime.datetime.now()
    refresh_token: Optional[str] = ''
    is_account_active: bool = False
    is_banned: bool = False
    token: Optional[str] = ''
    user_id: Indexed(str, unique=True)

    fname: str
    lname: str
    branch: Optional[str] = None
    gender: str
    email: Indexed(str, unique=True) 
    phone: Optional[str] = None
    standard: int
    wrong_answers: Optional[List[str]] = []

    tests:  Optional[List[ExamModel]] = []

    class Settings:
        name = "user"