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
- [To Do](#to-do)

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

*Order from newest to oldest.*

### 02/10/2024

- Add feature: MySQL explainer
- Edit feature: MYSQL explainer's prompt clean up

### 14/09/2024

- Initialize: README documentation
- Add feature: read database schemas from file
- Add feature: convert database schemas to JSON format (using hand code)
- Edit feature: convert database schemas to JSON format using AI
- Add feature: convert JSON format database schemas to markdown JSON format
- Add feature: MySQL generation
- Edit feature: MySQL generation's prompt edit
- Edit feature: MySQL generation's prompt clean up

### 13/09/2024

- Initialize: database utils
- Testing: `raw` vs `raw_output`
- Testing: modular design with CrewAI
- Testing: using `raw_output` with modular design

### 12/09/2024

- CrewAI is built upon LangChain, so CrewAI can use LangChain functions and tools (at least some of it).

  - https://docs.crewai.com/.

- In CrewAI, there 4 components that are important, they are `Agent()`, `Task()`, `Process()` and `Crew()`. However, only `Agent()`, `Task()` and `Process()` are worth keeping an eye on.

  - `Process()`: There are 2 types of process being **sequential** and **hierarchy**. However, it's **sequential** by defaultt.

  - `Agent()`: Initialize and declare your LLMs to use in the task.

  - `Task()`: This is the most important part. `Task()` is where most of the process' tasks are done. The output of 1 task is automatically used as the input of the next task but you can use the `context` keyword to force this flow. The `context` keyword is also used to dictate which tasks will be used as input of another task.

    - The output of 1 task is automatically used as the input of the next one. However, you can specify which task(s)
      should be used in another task, this could lead to 1 task using multiple tasks for its context. An `Agent` can be used by multiple `Task`(s) but those `Task`(s) must be performing the same operation. For example, `analyze_agent` can be used by both `business_analyze` and `market_analyze` because they perform the same operation, but `image_generate` cannot.

  - `Crew()`: This is where you will assemble your agents and tasks (list which agents and tasks are used in the process). The order in which the tasks are placed in `Crew()` will be the order that the tasks will perform (because it's **sequential** by default). Because the important components are the tasks not the agents, this means you can have a dispoportion for the agents and the tasks where an agent are used to perform for 2 tasks. `Crew()` is not that important, it's just a collection that house agents and tasks.

- In the CrewAI docs, these are the sections you need to view:

  - From `Core Concepts`: Agent, Task, Process, Crew and Tool (maybe)

  - From `How to Guides`: Sequential Process Overview -> Implementing Sequential Process and Hierarchical Process Overview (maybe)

  - From `Examples`: Look over some example code and you will see some a crew that have multiple task but fewer agent

### 11/09/2024

- Initialize: the 2nd initializattion of the project

### 08/08/2024

- Initialize: the project

---

## To Do:

- Add few-shot examples
