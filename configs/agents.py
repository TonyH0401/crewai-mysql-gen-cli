import os
from textwrap import dedent
from crewai import Agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()


class MySQLGenerateAgent:
    def __init__(self):
        GROQ_API = os.getenv("GROQ_API", "")
        self.llm = ChatGroq(api_key=GROQ_API, model="llama3-8b-8192")
        # self.llm = ChatGroq(api_key=GROQ_API, model="llama3-70b-8192")
        # self.llm = ChatGroq(api_key=GROQ_API, model="gemma2-9b-it")

    def mysql_generate_agent(self):
        return Agent(
            role="MySQL Expert",
            goal=dedent("""\
                Analyze the user specifications and database schemas information, generate syntactically correct MySQL query 
                based on the specifications and information while adhering to strict guidelines."""),
            backstory=dedent("""\
                As a MySQL Expert, you have extensive experiences with creating syntactically correct and efficient MySQL query,
                you specialize in creating syntactically correct MySQL query and evaluating MySQL query while adheres to rules
                set by the database schemas."""),
            allow_delegation=False,
            llm=self.llm,
            verbose=True,
        )

    def mysql_explain_agent(self):
        return Agent(
            role="MySQL Specialist",
            goal=dedent("""\
                Analyze the user specifications, database schemas information and MySQL code block. Based on the analyzation,
                create detail explanation which is clear, easy to understand and precise on the operation process."""),
            backstory=dedent("""\
                As a MySQL Specialist, you have extensive knowledge about MySQL, you can explain the process of a MySQL code
                block process based on the user specifications, database schemas information and a provided MySQL code block.
                Your explanation is clear, easy to understand and precise."""),
            allow_delegation=False,
            llm=self.llm,
            verbose=True
        )

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
