def get_book_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def count_words(text: str) -> int:
    return len(text.split())

def lower_text(text: str):
    return text.lower()

def count_characters(lower_text: str) -> dict:
    fiction = lower_text
    frequency = {}
    for c in fiction:
        if c in frequency:
            frequency[c] += 1
        else:
            frequency[c] = 1
    return frequency

def sort_by_frequency(frequency: dict):
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    return sorted_frequency

def chars_to_dicts(freq: dict) -> list[dict]:
    items = []
    for ch, n in freq.items():
        if ch.isalpha():
            items.append({"char": ch, "num": n})

    def sort_on(d: dict) -> int:
        return d["num"]

    items.sort(key=sort_on, reverse=True)
    return items
