from fastapi import APIRouter
from app.schemas.research import ResearchRequest

#Create a router object
router= APIRouter()

@router.get(
    "/",
    tags=["Home"],
    summary="Home Endpoint",
    description="Returns a welcome message."
)

def home():
    #DocString
    """
    Home endpoint.
    
    Returns:
        dict:Welcome message.
    """
    return {
        "message": "Welcome to Live AI Research Assistant!"
    }

@router.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id":user_id
    }

@router.get("search")
def search(query: str):
    return {
        "search":query
    }

# @router.get("/research")
# def research(
#     topic: str,
#     max_sources:int = 5
# ):
#     return {
#         "topic": topic,
#         "max_sources": max_sources,
#         "status": "Research request received."
#     } 

@router.post("/research")
def create_research(request: ResearchRequest):
    return {
        "topic": request.topic,
        "max_sources": request.max_sources,
        "status": "Research request received."
    }