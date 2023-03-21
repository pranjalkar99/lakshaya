from summarizer import Summarizer
from sentence_mapping import get_nouns_multipartite,make_filtered_keys,tokenize_sentences,get_sentences_for_keyword,generate_question_options
model = Summarizer()
from making_mcq import apply_wordsense_conceptnet_v1
import uvicorn
import random
import re

from fastapi import FastAPI

app = FastAPI()

@app.post("/kuch_to_karta_hai")
async def process_text(text: str):
    result = model(text, min_length=60, max_length = 500 , ratio = 0.4)
    summarized_text = ''.join(result)
    keywords = get_nouns_multipartite(text)
    filtered_keys=make_filtered_keys(keywords,summarized_text)
    sentences = tokenize_sentences(summarized_text)
    keyword_sentence_mapping = get_sentences_for_keyword(filtered_keys, sentences)
    key_distractor_list= apply_wordsense_conceptnet_v1(keyword_sentence_mapping)
    # Create a dictionary to store the question and its options
    question_dict = {}
    answer=generate_question_options(key_distractor_list,keyword_sentence_mapping)
    
    return {"processed_QA": answer}

if __name__=="__main__":
    uvicorn.run(app,port = 8040)