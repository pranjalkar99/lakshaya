import asyncio
from os import environ

import motor
from api.models.user.user_model import UserModel
# from api.models.admin.admin_model import AdminModel
# from api.models.company.company_model import CompanyModel
# from api.models.company.company_post_model import CompanyPostModel
# from api.models.general_use_models import NotificationModel
# from api.models.student.skill_model import SkillsModel
# from api.models.student.student_model import StudentModel
# from api.models.training.training import TrainingModel, TrainingRegistrations
from beanie import init_beanie


async def database():

    # Create Motor client
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://localhost:27017/lakshaya"
    )
    # print(environ.get("PROD_DB_URI"))

    await init_beanie(
        database = client.lakshaya,
        document_models = [
            UserModel,
            # AdminModel,
            # CompanyModel,
            # CompanyPostModel,
            # StudentModel,
            # SkillsModel,
            # NotificationModel,
            # TrainingModel,
            # TrainingRegistrations
        ]
    )
   