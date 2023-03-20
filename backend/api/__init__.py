from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import errors
from os import environ, path
from firebase_admin import credentials
import firebase_admin
from api.config.database import database
from logging import log

import asyncio

from api.routes.user import user_get_routes, user_post_routes

cred = firebase_admin.credentials.Certificate("lakshaya_service_account_keys.json")
firebase = firebase_admin.initialize_app(cred)
print("Firebase initialized")
print(firebase.name)

BASE_DIR = path.abspath(path.dirname(__file__))

def create_app():

    description = """
    This is a REST API for Education AP. This API is used to manage the data of the Education AP website. 

    """

    # Initialize fastapi app
    app = FastAPI(
        title = "Education AP",
        description = description
    )

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.on_event("startup")
    async def startup_event():
        try:

            # Loading environment variables from environment file
            # load_dotenv(path.join(BASE_DIR, '.env'))
            
            # Connect with database
            await asyncio.wait_for(database(), timeout=60.0)
            print("STARTUP")

        except asyncio.TimeoutError as e:
            #TODO: log error and continuous retry
            log("DB Timeout")
            pass

        except errors.DuplicateKeyError as e:
            #TODO: Critical error, notify to admin and dev
            log("DUPLICATE")

        except Exception as e:
            #TODO: Notify admin

            print("EXCEPTION", e)


    # Triggers functions on shutdown
    @app.on_event("shutdown")
    async def shutdown_event():
        print("SHUTDOWN")

    @app.get("/")
    async def index():
        return {"message" : "running"}
    
    app.include_router(
        user_get_routes.construct_router(),
        prefix = "/user"
    )

    app.include_router(
        user_post_routes.construct_router(),
        prefix = "/user"
    )
    
    return app