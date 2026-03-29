from fastapi import APIRouter
from app.agents.primary_agent import primary_agent

router = APIRouter()

@router.post("/query")
def handle_query(request: dict):
    user_input = request.get("query")   # FIXED HERE
    
    if not user_input:
        return {"error": "No input provided"}

    response = primary_agent(user_input)

    return {
        "input": user_input,
        "response": response
    }

@router.get("/")
def root():
    return {"message": "App is running"}