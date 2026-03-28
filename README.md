# System Architecture Overview
### Main Components
#### Primary Agent (Coordinator)
- Built using ADK + Gemini
- Handles user query
- Decides which sub-agent/tool to call
#### Sub-Agents
- Task Agent → manages tasks
- Calendar Agent → manages schedule
- Notes Agent → manages notes
#### MCP Server
- Connects agents to tools (Track 2 requirement)
- Tools:
    - Task Tool
    - Calendar Tool
    - Notes Tool
#### Database (AlloyDB – Track 3)
- Stores:
    - Tasks
    - Events
    - Notes
- Supports:
    -SQL queries
    -Natural language → SQL
#### API Layer (Track 1)
- Exposed via HTTP endpoint
- Deployed on Cloud Run