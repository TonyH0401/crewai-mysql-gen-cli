from crewai import Agent
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()
from textwrap import dedent

GROQ_API = os.getenv("GROQ_API", "")


def groq_llama3_70b():
    model = ChatGroq(api_key=GROQ_API, model="llama3-70b-8192")
    return model


def groq_gemma2_9b_it():
    model = ChatGroq(api_key=GROQ_API, model="gemma2-9b-it")
    return model


def mysql_generate_agent(llm):
    return Agent(
        role="MySQL Expert",
        goal="Generate syntactically correct MySQL query based on user specifications while adhering to strict guidelines",
        backstory="""
            You are a MySQL expert with extensive experience in creating syntactically correct, precise and efficient MySQL query.
            Your expertise and skills ensures that every query generated is syntactically correct and adheres to the rules set 
            by the database schemas.
        """,
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def mysql_extract_agent(llm):
    return Agent(
        role="MySQL Query Extractor",
        goal="Extract MySQL query code block from a text passage while adhering to strict guidelines",
        backstory="""
            You are a MySQL extractor.
            You are responsible for extracting ONLY MySQL query code block from a text passage.
        """,
        verbose=True,
        allow_delegation=False,
        llm=llm
    )
