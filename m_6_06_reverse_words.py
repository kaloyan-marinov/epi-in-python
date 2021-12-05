def reverse_words(s: str) -> str:
    words = s.split(" ")
    new_s = " ".join(words[::-1])
    return new_s
