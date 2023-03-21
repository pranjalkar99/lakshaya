from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import errors
from os import environ, path
from firebase_admin import credentials
import firebase_admin
from api.config.database import database
from logging import log
from summarizer import Summarizer

from api.schemas.user.request_schemas import user_request_schemas
from api.models.user.user_model import UserModel

from api.utils.nlp.sentence_mapping import get_nouns_multipartite,make_filtered_keys,tokenize_sentences,get_sentences_for_keyword,generate_question_options
from api.utils.nlp.making_mcq import apply_wordsense_conceptnet_v1

# model_sum = Summarizer()


import asyncio

from api.routes.user import user_get_routes, user_post_routes

cred = firebase_admin.credentials.Certificate("lakshaya_service_account_keys.json")
firebase = firebase_admin.initialize_app(cred)
print("Firebase initialized")
print(firebase.name)

BASE_DIR = path.abspath(path.dirname(__file__))

model = Summarizer()

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
    
    @app.get('/{user_id}')
    async def get_user_profile(
        user_id: str
    ):
        print(user_id)
        response = await UserModel.find_one(
            UserModel.user_id == user_id
        )
        

        return response
    
    @app.post("/analyze-text")
    async def process_text(request: user_request_schemas.UserTextSummarySchema):
        print("it is running")
        result = model(request.transcript, min_length=60, max_length = 500 , ratio = 0.4)
        summarized_text = ''.join(result)
        keywords = get_nouns_multipartite(request.transcript)
        filtered_keys=make_filtered_keys(keywords,summarized_text)
        sentences = tokenize_sentences(summarized_text)
        keyword_sentence_mapping = get_sentences_for_keyword(filtered_keys, sentences)
        key_distractor_list= apply_wordsense_conceptnet_v1(keyword_sentence_mapping)
        # Create a dictionary to store the question and its options
        question_dict = {}
        answer=generate_question_options(key_distractor_list,keyword_sentence_mapping)
        
        return {"processed_QA": answer}
    
    app.include_router(
        user_get_routes.construct_router(),
        prefix = "/user"
    )

    app.include_router(
        user_post_routes.construct_router(),
        prefix = "/user"
    )
    
    return app