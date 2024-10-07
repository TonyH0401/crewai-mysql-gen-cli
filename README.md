# Optimized MySQL Query Generation with CrewAI and GroqAI on CLI (Version 03)

Welcome to the MySQL Query Generation Project with CrewAI and GroqAI!

This project serves as a comprehensive guide, offering testing and implementation insights for efficiently generating MySQL queries using CrewAI and GroqAI. This project is the 3rd version in a series of similar projects.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Virtual Environment](#Virtual-Environment)
  - [Installation](#installation)
  - [Environment Variable](#Environment-Variable)
- [Quick Start](#Quick-Start)
- [Development Documentation](#development-documentation)

## Introduction

This repository contains my implementation of CrewAI, an LLM framework, and GroqAI for MySQL Query Generation based User Specifications. Originally, it was planned for the database schemas to be a constant but I have changed it to reading the database schemas using files, it was later improved to reading from files and convert them into JSON format before processing them.

This project's functionalities include:

- MySQL Generation based on User Specifications.
- Question Recommendations based on User Database Schemas.

## Getting Started

I recommend running this project on **Python 3.10+**. This project was originally running on **Python 3.11.9**.

### Virtual Environment

A virtual environment should be setup for this project. You can use any of yours preferable virtual environment, I will use Anaconda/Miniconda as the Virtual Environment for this project.

### Installation

To get started, you need to download this project from Github and navigate to the project's folder.

```sh
cd crewai-mysql-gen-cli/
```

Dowloading the project's dependencies from `requirements.txt` file.

```sh
pip install -r requirements.txt
```

I also have a [link](https://chatgpt.com/share/757c50b4-f574-48d0-a04d-c955d100aeab) to support you in this process.

### Environment Variable

This step is **important**! Create an `.env` file to store your API KEY(s). These are the API KEY(s) you will need. Currently, in this project, I am using GroqAI API but you can change it to any LLM(s) you prefer.

```sh
GROQ_API=""
```

## Quick Start

The main functions are located in `main.py` and there are databases provided in the repository. Run the project using the following command(s).

```sh
python main.py
```

Inside `main.py`, there are 2 crews, these are for the 2 main functions of this project, you can comment out the function you don't want to run.

```sh
print(">>> Question Suggest Program starts!")
output = query_suggest_crew.kickoff()
print(">>> Question Suggest Answer:")
print(output)
# print(">>> Program 2 starts!")
# output = mysql_crew.kickoff()
# print(">>> Answer:")
# print(output)
# print(">>> MySQL code block only:")
# print(mysql_generate_task.output.raw_output)
```

You can provide your own databases in the `mysql_db_schemas/` directory. You can load them in `main.py` by changing the file path.

```sh
filepath = "./mysql_db_schemas/{your-database-name}.sql"
```

---

## Development Documentation

Order from newest to oldest.

### 07/08/2024

- Create `mysql_gen_v02`.
- Change prompts, add MySQL files.

### 06/08/2024

- Push old prompts, link can be found [here](https://github.com/TonyH0401/langchain-groq-mysql-query-gen-cli/tree/5cfaf064e1bd35802900da10ff3997c22b2af424).

CrewAI is built upon LangChain, so CrewAI can use LangChain functions and tools (some of it).

This a MySQL Generator using CrewAI and Groq, it is also a CrewAI guide for beginner.

- https://docs.crewai.com/.

There are 4 things in CrewAI that are important: Agent, Task, Process and Crew. However, only Agent, Task and Process are the most important.
And from those 3 only Task is the most important

CrewAI the important is not the agent, the important is the task, that means you can have a dispoportion for the agent and task
the agent and task must be in sequence (regardless of process sequential or process hierarchy)
the crew is just a collection of agent and task (this is more important) to kickoff

A collection of notes for CrewAI: - In CrewAI, this is the order that is the most important, start from least to most (my opinion): - Crew, this is just a collection representing what will be used for an operation. - Process - Agent, - Task - In CrewAI, the output of 1 task is automatically used as the input of the next one. However, you can specify which task(s)
should be used in another task, this could lead to 1 task using multiple tasks for its context. - An `Agent` can be used by multiple `Task`(s) but those `Task`(s) must be performing the same operation. For example,
`analyze_agent` can be used by both `business_analyze` and `market_analyze` because they perform the same operation, but
`image_generate` cannot.

In the CrewAI docs, these are the sections you need to view: - Agent - Task - Process - Crew - Tool (maybe)
How to Guides - Sequential Process Overview > Implementing Sequential Process - Hierarchical Process Overview
Examples: Look over some example code and you will see some a crew that have multiple task but fewer agent

TO-DO:

- Add few-shot examples
