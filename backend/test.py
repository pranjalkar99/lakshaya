from summarizer import Summarizer
# from fastapi import FastAPI
model_sum = Summarizer()
def analyze_f(text:str):
    model_sum = Summarizer()
    result = model_sum(text, min_length=60)

    return result
    # print(result)
    # questions = []
    # fully = ''.join(result)
    # full = fully.split(".")
    # dic = await get_sentence_keypair(full)

    # for sentence in dic.keys():
    #     for key in dic[sentence]:

    #         questions.append(get_question(key,sentence))
    #         for each_question in questions:
    #             qa[each_question]=run_QA_inference(each_question,fully)

# app=FastAPI()


