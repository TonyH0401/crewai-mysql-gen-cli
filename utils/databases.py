from crewai import Agent, Task, Crew, Process
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()


def read_mysql_db(filepath):
    raw_schemas = None
    try:
        file_exist = os.path.isfile(filepath)
        if file_exist is False:
            print(">>> File does not exist!")
            return None
        fd = open(filepath, "r")
        mysql_file = fd.read()
        raw_schemas = mysql_file
        fd.close()
    except Exception as e:
        print(f">>> Exception Message: {e}")
    return raw_schemas


def convert_schemas_to_json_markdown(raw_schemas):
    GROQ_API = os.getenv("GROQ_API", "")
    llm = ChatGroq(api_key=GROQ_API, model="llama3-8b-8192")

    return None

# def
