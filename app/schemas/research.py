from pydantic import BaseModel, Field

class ResearchRequest(BaseModel):
    topic: str = Field(
        ..., #It means it is necessary
        min_length=3,
        max_length=200,
        description="The research topic to investigate."
    )
    max_sources: int = Field(
        default=5,
        ge=1,
        le=20,
        description="Maximum number of sources to investigate."
    ) 
    language: str = "English"
    verify_sources: bool = True 