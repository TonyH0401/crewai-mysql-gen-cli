from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API = os.getenv("GROQ_API", "")


def groq_llama3_70b():
    model = ChatGroq(api_key=GROQ_API, model="llama3-70b-8192")
    return model


def groq_gemma2_9b_it():
    model = ChatGroq(api_key=GROQ_API, model="gemma2-9b-it")
    return model
