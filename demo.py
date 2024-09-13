from textwrap import dedent
from langchain_groq import ChatGroq
from crewai import Agent, Task, Crew, Process
import os
from dotenv import load_dotenv
load_dotenv()

# Define LLM
GROQ_API = os.getenv("GROQ_API", "")
llm = ChatGroq(api_key=GROQ_API, model="llama3-8b-8192")
# llm = ChatGroq(api_key=GROQ_API, model="llama3-70b-8192")
# llm = ChatGroq(api_key=GROQ_API, model="gemma2-9b-it")

# Define user question, must be precise
user_specs = "Tell me a joke about dogs."

# Define agent
comedian_agent = Agent(
    role="Expert Comedian",
    goal=dedent("""\
        Analyze the user input to extract the neccessary information. From the information, create a joke that is
        funny and short."""),
    backstory=dedent("""\
            As an expert in comedy, you have deep understanding on how a joke should be performed and delivered.
            The joke you create are short but they are informative and funny."""),
    allow_delegation=False,
    llm=llm,
    verbose=True
)
audience_agent = Agent(
    role="Performance Expert",
    goal=dedent("""\
        Analyze the performance, explain what is the meaning of the performance. Evaluate the performance, 
        give the performance a score on a scale of 1 to 10 and explain why the score was give based on
        what criteria."""),
    backstory=dedent("""\
            You are an audience, specialized in evaluating the performance of artists. You explain the
            meaning of the performance. You give scores to the performance based on certain criteria."""),
    allow_delegation=False,
    llm=llm,
    verbose=True,
)

# Define task
joke_generate_task = Task(
    description=dedent(f"""\
        Given the information about the user specifications, analyze the user input and extract the neccessary information,
        no yapping:
            User input: {user_specs}.
        
        Based on the information generate short but funny joke about the provided topic. No yapping.
        
        The final result is a string which is a joke. No yapping."""),
    expected_output=dedent("""\
            A string which is the joke based on the user specifications.
        """),
    agent=comedian_agent,
)
evaluate_task = Task(
    description=dedent("""\
        Based on the performance result, analyze the performance, explain what is the meaning of the performance.
        No yapping.
        
        Evaluate the performance, give the performance a score on a scale of 1 to 10 and explain why the score 
        was give based on what criteria. No yapping."""),
    expected_output=dedent("""\
        Three paragraphs seperated.
        The first paragraph display the original performance.
        The second paragraph is the explanation of the performance.
        The second paragraph is the score given for the performance with criteria."""),
    agent=audience_agent,
    # context=[generate_task]
)

# Define comedian crew
crew = Crew(
    agents=[comedian_agent, audience_agent],
    tasks=[joke_generate_task, evaluate_task],
    verbose=True,
    process=Process.sequential
)
output = crew.kickoff()

print(">>> Output:")
print(output)

# print(">>> Raw query:\n", generate_task.output.raw_output)
