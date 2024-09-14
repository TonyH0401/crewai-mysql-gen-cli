from textwrap import dedent
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
    json_agent = Agent(
        role="Information Extractor Expert",
        goal=dedent("""\
            Extract information from columns provided by the schemas. Convert the extracted information into JSON format."""),
        backstory=dedent("""\
            As an Information Extractor Expert, you have extensive experiences with extracting information from the 
            provided schemas and category them in the correct JSON format."""),
        allow_delegation=False,
        llm=llm,
        # verbose=True,
    )
    json_convert_task = Task(
        description=dedent(f"""\
            Given the information about the database schemas, analyze the database, focus on identifying information of 
            the database schemas:    
                - Schemas: {raw_schemas}

            Extract the information from database schemas. Strictly follow these goals and rules below. No yapping.
            DO NOT make up information. DO NOT skip this step.
                - DO:
                    - The schema table name is the JSON object name.
                    - Each column is a property in the JSON object.
                    - The value of each property is the datatype of each column.
                    - Include property for "PRIMARY KEY" and "CONSTRAINT".
                    - Extract the column information from the schemas and return the extracted data in JSON format.
                    - Return ONLY the JSON format.
                - DO NOT:
                    - Add "Here is the extracted data in JSON format:" or any similar lines. 

            The final result is a JSON object containing the converted information of the database schemas."""),
        expected_output=dedent("""\
            A JSON object containing the converted information of the database schemas."""),
        agent=json_agent
    )
    json_convert_crew = Crew(
        agents=[json_agent],
        tasks=[json_convert_task],
        # verbose=True,
        process=Process.sequential
    )
    output = json_convert_crew.kickoff()
    json_markdown = f"""```mysql\n {output} \n```"""
    return json_markdown
