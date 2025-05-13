from app.logic import sentiment, readability, suggestions
from app.models.schemas import ReviewResponse

def analyze_review(content: str) -> ReviewResponse:
    return ReviewResponse(
        sentiment=sentiment.get_sentiment(content),
        readability_score=readability.get_readability(content),
        suggestions=suggestions.get_suggestions(content),
    )
