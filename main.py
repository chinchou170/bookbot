from stats import (
    get_book_text,
    count_words,
    lower_text,
    count_characters,
    chars_to_dicts,
)

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = count_words(text)
    lowered = lower_text(text)
    frequency = count_characters(lowered)
    sorted_char_dicts = chars_to_dicts(frequency)

    print(f"============ BOOKBOT ============\n Analyzing book found at {path}...\n ----------- Word Count ----------\n Found {num_words} total words\n --------- Character Count -------\n")
    for entry in sorted_char_dicts:
        print(f"{entry['char']}: {entry['num']}")
    print(f"============= END ===============")

if __name__ == "__main__":
    main()