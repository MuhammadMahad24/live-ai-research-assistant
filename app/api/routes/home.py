from fastapi import APIRouter,HTTPException
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
    
    if user_id <=0:
        raise HTTPException(
            status_code=400,
            detail="User ID must be greater than 0."
        )
    if user_id > 10:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )
    
    
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
    
    if request.topic.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Research topic cannot be empty."
        )
    
    
    return {
        "topic": request.topic,
        "max_sources": request.max_sources,
        "status": "Research request received."
    }
    