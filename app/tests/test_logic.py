from app.logic import sentiment, readability, suggestions

def test_sentiment():
    assert sentiment.get_sentiment("This is bad") == "negative"
    assert sentiment.get_sentiment("This is good") == "positive"
    assert sentiment.get_sentiment("This is okay") == "neutral"

def test_readability():
    assert readability.get_readability("This is a sentence.") > 0

def test_suggestions():
    assert "Expand" in suggestions.get_suggestions("Too short")[0]
