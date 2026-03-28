from fastapi import APIRouter
from agents.primary_agent import primary_agent

router = APIRouter()

@router.post("/query")
def handle_query(request: dict):
    user_input = request.get("user_input")
    
    if not user_input:
        return {"error": "No input provided"}

    response = primary_agent(user_input)

    return {
        "input": user_input,
        "response": response
    }