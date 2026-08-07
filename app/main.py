from fastapi import FastAPI
from app.api.routes.home import router as home_router
app= FastAPI(
    title="Live AI Research Assistant API", #Name of project
    description="", #explains API
    version="1.0.0"
)

# @app.get("/",
#         tags=["Home"],
#         summary="Home Endpoint",
#         description="Returns a welcome message."
#         )
# def home():
#     """
#     Home endpoint 
#     Returns: 
#          dict: Welcome message.
#     This function runs when a clients sends
#     a GET request to the root URL.
#     """
#     return {
#         "message": "Welcome to Live AI Research Assistant!"
#     }

#Register the router with the FastAPI application
app.include_router(home_router)