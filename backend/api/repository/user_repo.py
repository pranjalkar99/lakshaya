import json
from api.utils.exceptions import exceptions
from fastapi.responses import JSONResponse
import os

from summarizer import Summarizer
# from api.utils.sentence_mapping import get_nouns_multipartite,make_filtered_keys,tokenize_sentences,get_sentences_for_keyword,generate_question_options
from api.utils.nlp.sentence_mapping import get_nouns_multipartite,make_filtered_keys,tokenize_sentences,get_sentences_for_keyword,generate_question_options

# model = Summarizer()
from api.utils.nlp.making_mcq import apply_wordsense_conceptnet_v1

import random
import re
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from summarizer import Summarizer
from api.utils.nlp.qna import get_sentence_keypair, run_QA_inference
from api.drivers.user import user_drivers
from api.schemas.user.response_schemas import user_response_schema
# import model_sum
# from api import model_sum

model_sum = Summarizer()

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
def merge(list1):
        merged_list = []
        for element in list1:
            if type(element) == list:
                merged_list.extend(element)
            else:
                merged_list.append(element)
        return merged_list

def is_authenticated_and_authorized(request, authorization):

    # Check if user is authenticated and authorized
    if not authorization["flag"]:
        raise exceptions.AuthenticationError()

    if authorization["token"] != request["student_id"]:
        raise exceptions.UnauthorizedUser(authorization["token"])


async def get_info(request, authorization):
    try:
        if type(request) == dict:
            is_authenticated_and_authorized(request, authorization)
        else:
            is_authenticated_and_authorized(request.__dict__, authorization)

        # Executes student instance method
        # response = await fn(request)
        response = "it is definiteky working"

        if response:
            return JSONResponse(status_code=200,
                                content={"message": "student information updated"})

        return JSONResponse(status_code=200,
                            content={"message": "student information cannot be updated"})

    except exceptions.AuthenticationError as e:

        return JSONResponse(status_code=403,
                            content={"message": authorization["message"]})

async def get_user_profile_handler(user_id):
    try:

        response = await user_drivers.User().get_user_profile(user_id)

        if not response:
            return JSONResponse(
                status_code=404,
                content={
                    "message" : "user not found"
                }
            )
        
        
        return JSONResponse(
            status_code=200,
            content = json.loads(
                json.dumps(
                    user_response_schema
                    .UserDataSchema(**response).__dict__, 
                    default=lambda o: o.__dict__
                )
            )
        )

        
    except exceptions.AuthenticationError as e:

        return JSONResponse(status_code=403, 
            content={"message" : "message"})
