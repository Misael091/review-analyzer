def get_readability(text: str) -> float:
    words = text.split()
    sentences = text.count('.') + text.count('!') + text.count('?')
    if sentences == 0:
        sentences = 1
    return round(len(words) / sentences, 2)
