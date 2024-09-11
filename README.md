CrewAI is built upon LangChain, so CrewAI can use LangChain functions and tools (some of it).
This a MySQL Generator using CrewAI and Groq, it is also a CrewAI guide for beginner.
    - https://docs.crewai.com/.

There are 4 things in CrewAI that are important: Agent, Task, Process and Crew. However, only Agent, Task and Process are the most important.
And from those 3 only Task is the most important

CrewAI the important is not the agent, the important is the task, that means you can have a dispoportion for the agent and task
the agent and task must be in sequence (regardless of process sequential or process hierarchy)
the crew is just a collection of agent and task (this is more important) to kickoff 


In crewAI, the output of one task is automatically used for the next one (by default). However, you can specify which one you want

In the CrewAI docs, these are the sections you need to view
    - Agent
    - Task
    - Process
    - Crew
    - Tool (maybe)
    How to Guides
        - Sequential Process Overview > Implementing Sequential Process 
        - Hierarchical Process Overview
    Examples: Look over some example code and you will see some a crew that have multiple task but fewer agent