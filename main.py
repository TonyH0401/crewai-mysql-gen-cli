from mysql_db_schema import SCHEMA
from crewai import Crew, Process
from configs.agents import MySQLGenerateAgent
from configs.tasks import MySQLGenerateTasks

# Define user question, must be precise
user_specs = "List popular Electronics products"

# Initialize Agents and Tasks
agents = MySQLGenerateAgent()
tasks = MySQLGenerateTasks()

# Create Agents
mysql_generate_agent = agents.mysql_generate_agent()
# Create Tasks
mysql_generate_task = tasks.mysql_generate_task(
    mysql_generate_agent, SCHEMA, user_specs)

# Create Crew for MySQL generation
mysql_crew = Crew(
    agents=[mysql_generate_agent],
    tasks=[mysql_generate_task],
    verbose=True,
    process=Process.sequential
)

if __name__ == "__main__":
    print(">>> Program starts!")
    output = mysql_crew.kickoff()
    print(">>> Answer:")
    print(output)
