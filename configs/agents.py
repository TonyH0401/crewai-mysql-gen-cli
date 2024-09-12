import os
from textwrap import dedent
from crewai import Agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()


class PoemGenerateAgent:
    def __init__(self):
        GROQ_API = os.getenv("GROQ_API", "")
        self.llm = ChatGroq(api_key=GROQ_API, model="llama3-8b-8192")
        # self.llm = ChatGroq(api_key=GROQ_API, model="llama3-70b-8192")
        # self.llm = ChatGroq(api_key=GROQ_API, model="gemma2-9b-it")

    def poem_generate_agent(self):
        return Agent(
            role="Poem Expert",
            goal=dedent("""\
                    Analyze keywords and request from the user,
                    generate a poem based on the user specifications and requirements."""),
            backstory=dedent("""\
                    You are famous Poet living in Acient Greek,
                    you specialize in making beautiful poems (both long and short poems) with deep meaning."""),
            allow_delegation=False,
            llm=self.llm,
            verbose=True,
        )

    # def mysql_generate_agent(self):
    #     return Agent(
    #         role="MySQL Expert",
    #         goal="Generate syntactically correct MySQL query based on user specifications while adhering to strict guidelines",
    #         backstory="""
    #             You are a MySQL expert with extensive experience in creating syntactically correct, precise and efficient MySQL query.
    #             Your expertise and skills ensures that every query generated is syntactically correct and adheres to the rules set
    #             by the database schemas.
    #         """,
    #         allow_delegation=False,
    #         llm=self.llm,
    #         verbose=True,
    #     )

    # def mysql_extract_agent(llm):
    #     return Agent(
    #         role="MySQL Query Extractor",
    #         goal="Extract MySQL query code block from a text passage while adhering to strict guidelines",
    #         backstory="""
    #             You are a MySQL extractor.
    #             You are responsible for extracting ONLY MySQL query code block from a text passage.
    #         """,
    #         verbose=True,
    #         allow_delegation=False,
    #         llm=llm
    #     )
