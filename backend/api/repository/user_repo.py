import json
from api.utils.exceptions import exceptions
from fastapi.responses import JSONResponse
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from summarizer import Summarizer
from api.utils.nlp.qna import get_sentence_keypair, run_QA_inference

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


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


async def analyze_text(request):
    qa = {}
    model_sum = await Summarizer()
    # print(request.transcript)

    result = await model_sum(request.transcript, min_length=60)
    print(result)
    questions = []
    fully = ''.join(result)
    full = fully.split(".")
    dic = await get_sentence_keypair(full)

    # for sentence in dic.keys():
    #     for key in dic[sentence]:

    #         questions.append(get_question(key,sentence))
    #         for each_question in questions:
    #             qa[each_question]=run_QA_inference(each_question,fully)

    response = {"result of Summary": fully, "keypair": dic, "questions": questions, "qa": qa}
    print(response)

    return response
