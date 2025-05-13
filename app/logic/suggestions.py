def get_suggestions(text: str) -> list[str]:
    suggestions = []
    if len(text) < 20:
        suggestions.append("Expand your review to give more details.")
    if "very" in text.lower():
        suggestions.append("Avoid overused words like 'very'.")
    return suggestions
