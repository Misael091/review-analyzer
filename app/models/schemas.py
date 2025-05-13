from pydantic import BaseModel

class ReviewRequest(BaseModel):
    content: str

class ReviewResponse(BaseModel):
    sentiment: str
    readability_score: float
    suggestions: list[str]
