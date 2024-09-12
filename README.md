CrewAI is built upon LangChain, so CrewAI can use LangChain functions and tools (some of it).
This a MySQL Generator using CrewAI and Groq, it is also a CrewAI guide for beginner.
    - https://docs.crewai.com/.

There are 4 things in CrewAI that are important: Agent, Task, Process and Crew. However, only Agent, Task and Process are the most important.
And from those 3 only Task is the most important

CrewAI the important is not the agent, the important is the task, that means you can have a dispoportion for the agent and task
the agent and task must be in sequence (regardless of process sequential or process hierarchy)
the crew is just a collection of agent and task (this is more important) to kickoff 

A collection of notes for CrewAI:
    - In CrewAI, this is the order that is the most important, start from least to most (my opinion):
        - Crew, this is just a collection representing what will be used for an operation. 
        - Process
        - Agent,
        - Task
    - In CrewAI, the output of 1 task is automatically used as the input of the next one. However, you can specify which task(s)
    should be used in another task, this could lead to 1 task using multiple tasks for its context. 
    - An `Agent` can be used by multiple `Task`(s) but those `Task`(s) must be performing the same operation. For example,
    `analyze_agent` can be used by both `business_analyze` and `market_analyze` because they perform the same operation, but
    `image_generate` cannot.  

In the CrewAI docs, these are the sections you need to view:
    - Agent
    - Task
    - Process
    - Crew
    - Tool (maybe)
    How to Guides
        - Sequential Process Overview > Implementing Sequential Process 
        - Hierarchical Process Overview
    Examples: Look over some example code and you will see some a crew that have multiple task but fewer agent