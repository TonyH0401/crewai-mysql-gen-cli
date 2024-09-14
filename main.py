from crewai import Crew, Process
from configs.agents import MySQLGenerateAgent
from configs.tasks import MySQLGenerateTasks
from utils.databases import read_mysql_db, convert_schemas_to_json_markdown
import sys

# Reading database filepath
demo = ".zookeeper.sql"
filepath = "./mysql_db_schemas/employee.sql"
raw_schemas = read_mysql_db(filepath)
if raw_schemas is None:
    print(">>> Closing the program. Please use the correct file path!")
    sys.exit()

# Convert raw schemas to json markdown
schemas_json_markdown = convert_schemas_to_json_markdown(raw_schemas)

# Define user question, must be precise
user_specs = "How many employees are there?"

# Initialize Agents and Tasks
agents = MySQLGenerateAgent()
tasks = MySQLGenerateTasks()

# Create Agents
mysql_generate_agent = agents.mysql_generate_agent()
# Create Tasks (important)
mysql_generate_task = tasks.mysql_generate_task(
    mysql_generate_agent, schemas_json_markdown, user_specs)

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
