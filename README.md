# Multi-Agent Productivity Assistant

A scalable AI-powered multi-agent system built using FastAPI and deployed on Google Cloud Run. This application enables users to manage tasks, notes, and calendar events through a single intelligent API interface.

---

## Project Overview

The Multi-Agent Productivity Assistant simulates a real-world AI agent ecosystem where multiple specialized agents collaborate to handle user queries:

- Task Management Agent  
- Notes Management Agent  
- Calendar Scheduling Agent  

The system processes natural language queries and routes them to the appropriate agent(s), supporting both single-step and multi-step instructions.

---

## Features

- Multi-agent architecture (Task, Notes, Calendar)
- Natural language query handling
- Multi-step query execution
- REST API with FastAPI
- PostgreSQL (AlloyDB) integration
- Cloud-native deployment (Google Cloud Run)
- Modular and scalable backend design

---

## Architecture

User Query → Primary Agent → Routing Logic  
→ Task Agent → Database  
→ Notes Agent → Database  
→ Calendar Agent → Database  

---

## Tech Stack

- Backend: FastAPI  
- Language: Python 3.12  
- Database: PostgreSQL (Google AlloyDB)  
- Deployment: Google Cloud Run  
- Containerization: Docker  
- Database Driver: psycopg2  

---

## Live Deployment /API Endpoint

### Cloud Run Service URL:
URL
https://multi-agent-app-967032033550.asia-south1.run.app  



### Endpoint
POST /query  

### Request Format
```json
{
  "query": "create task complete project"
}

Response Format
{
  "input": "create task complete project",
  "response": ["Task created successfully"]
}

Example Queries

Task Agent
{ "query": "create task complete project" }
{ "query": "show tasks" }

Notes Agent
{ "query": "add note learn MCP" }
{ "query": "show notes" }

Calendar Agent
{ "query": "schedule meeting tomorrow" }
{ "query": "show events" }

Multi-Agent Query
{
  "query": "create task finish report and add note important work and schedule meeting"
}

```

Local Setup

1. Clone Repository
git clone https://github.com/MJanbandhu/Multi-Agent-Productivity-Assistant.git 
cd Multi-Agent-Productivity-Assistant

2. Create Virtual Environment
python -m venv .venv
source .venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file in the root directory:

DB_HOST=your-db-host
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=your-password
DB_PORT=5432

5. Run the Application
uvicorn app.main:app --reload

Deployment (Cloud Run)

gcloud run deploy multi-agent-app \
--source . \
--region asia-south1 \
--allow-unauthenticated \
--set-env-vars DB_HOST=...,DB_NAME=...,DB_USER=...,DB_PASSWORD=...,DB_PORT=5432

Project Structure

```
app/
├── agents/
│   ├── primary_agent.py
│   ├── task_agent.py
│   ├── notes_agent.py
│   ├── calendar_agent.py
│
├── api/
│   └── routes.py
│
├── db/
│   ├── connection.py
│   └── queries.py
│
├── tools/
│   ├── task_tool.py
│   ├── notes_tool.py
│   ├── calendar_tool.py
│
├── mcp/
│   ├── server.py
│   └── tool_registry.py
│
└── main.py
``` 

Future Improvements

LLM-based intent detection (replace keyword-based routing)
User authentication and session handling
Frontend interface (React or Streamlit)
Advanced scheduling and parsing logic
Async database operations
Logging and monitoring



Author

Mohit Janbandhu












