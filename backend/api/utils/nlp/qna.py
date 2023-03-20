from summarizer import Summarizer
from tqdm import tqdm
import sqlite3
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
# from us import get_transcript_v3
# from ques_trans import get_question
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

def run_QA_inference(question, context, model_name="deepset/roberta-base-squad2"):
    # Load model & tokenizer
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Get predictions
    nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
    QA_input = {'question': question, 'context': context}
    res = nlp(QA_input)

    return res

def get_sentence_keypair(sentences):
    keyword_mapping = {}

    # process each sentence
    for sentence in sentences:
        
        # tokenize sentence into words
        words = word_tokenize(sentence.lower())
        words = [word for word in words if word not in stopwords.words('english')]

        # remove stopwords
        

        # initialize keyword list for sentence
        sentence_keywords = []

        for word in words:
            if word.isalpha():  # only consider words that contain alphabets
                sentence_keywords.append(word)

        # find keywords in sentence
        

        # add keywords to mapping
        keyword_mapping[sentence] = sentence_keywords

    return keyword_mapping