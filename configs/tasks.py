from crewai import Task
from textwrap import dedent


class MySQLGenerateTasks:
    def sql_question_suggest_task(self, agent, db_specs):
        return Task(
            description=dedent(f"""\
                Given the information about the database schemas, analyze the database schemas, focus on identifying features 
                and information of the database schemas and the overall narrative presented:
                    - Database schemas information: {db_specs}.

                Generate 4 meaningful and informative questions ONLY based on the information from the database schemas.
                You DO NOT generate questions that perform DML operations such as `INSERT`, `UPDATE` and `DELETE`.
                No yapping. DO NOT skip this step.

                The final result is an array with 4 recommended questions ONLY. No yapping."""),
            expected_output=dedent("""\
                An array with 4 recommended questions ONLY and there will be no explanation or comment."""),
            agent=agent
        )

    def mysql_generate_task(self, agent, db_specs, user_specs):
        return Task(
            description=dedent(f"""\
                Given the information about the database and user specifications, analyze the database and user specifications,
                focus on identifying features and information of the database schemas and user specifications and the overall
                narrative presented:
                    - Database schemas information: {db_specs}.
                    - User specifications: {user_specs}.

                Generate MySQL query based on the user specifications and information from the database schemas while 
                strictly adhering to the following rules. No yapping:
                    - DO:
                        - ALWAYS look at the tables and tables' properties in the database schemas to see what you can query,
                        use ONLY the column names you can see existing in the table schemas, use ONLY the column names needed
                        to asnwer the user specifications.
                        - Pay attention to which columns is in which tables, the name in the generated query MUST be the same
                        as the names of the tables and columns in the database schemas.
                        - Order the results to return the most informative data in the database, ALWAYS use the primary key(s)
                        in 'SELECT' query,
                        - Unless the user specifies in the question which specific columns to obtain, display for at 
                        most 5 significant columns ONLY.
                        - Use function to get the current date, if the question involves "today".
                        - ALWAYS use 'JOIN' to join multiple tables.
                        - When 'GROUP BY', check if there are enough essential columns.
                        - ALWAYS use 'LIMIT' to limit to 10 rows.
                    DO NOT skip this step.
                    - DO NOT:
                        - Change the table and column names.
                        - Create query for tables and columns that do not exist.
                        - Use MySQL subquery.
                        - Use 'SELECT *', 'TOP 1'.
                    DO NOT skip this step.

                The final result is a MySQL query code block ONLY, there will be no explanation or comment on the
                MySQL code block. No yapping."""),
            expected_output=dedent("""\
                An syntactically correct and optimal MySQL query inside a markdown code block like this ```sql ```.
                There will be no explanation or comment on the MySQL code block."""),
            agent=agent
        )

    def mysql_explain_task(self, agent, db_specs, user_specs, *context):
        return Task(
            description=dedent(f"""\
                Given the information about the provided database schemas, user specifications and MySQL code block;
                analyze the provided database schemas information, user specifications and MySQL code block:
                    - Database schemas information: {db_specs}.
                    - User specifications: {user_specs}.

                Based on the analysis of the database schemas, user specifications and MySQL code block, generate
                an explanation about the MySQL code block (process). No yapping.

                The final result consists of two parts:
                    - **MySQL code block**: A MySQL code block contained inside a ```sql ``` markdown.
                    - **Explain**: A paragraph contains the explanation."""),
            expected_output=dedent("""\
                The final result consists of two parts:
                    - **MySQL code block**: A MySQL code block contained inside a ```sql ``` markdown.
                    - **Explain**: A paragraph contains the explanation."""),
            agent=agent,
            context=list(context)
        )


# # Define task
# extract_task = Task(
#     description="""
#             Strictly adhering to the following rules:
#                 - Receive the output from 'generator' agent and extract ONLY the SQL queries code block.
#                 - Place the SQL queries code block inside this format ```sql ```.
#                 - Below the ```sql ``` is the explaination for the SQL queries code block.
#                 Do NOT skip this step.
#         """,
#     agent=extract_agent,
#     expected_output="""
#             SQL queries code block generated by 'generator' agent in this ```sql ``` format.
#             With SQL queries code block exaplaination.
#         """,
#     context=[generate_task]
# )
