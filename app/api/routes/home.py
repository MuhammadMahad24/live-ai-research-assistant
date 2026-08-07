from fastapi import APIRouter

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
    