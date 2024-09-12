from crewai import Task
from textwrap import dedent


class PoemGenerateTasks:
    def poem_generate_task(self, agent, user_specs):
        return Task(
            description=dedent(f"""\
                Analyze the given user specifications: {user_specs}.
                Focus on identifying unique features and the overall narrative presented.
                
                Generate a poem based on the analyzed user specifications.
                Your poem must be elegant, informative and exciting to the reader.
                
                The final result is ONLY the poem, no yapping."""),
            expected_output=dedent("""\
                Display the poem based on the user specifications.
                If there aren't any specifications, display the poem in paragraphs with spaces between."""),
            agent=agent
        )
