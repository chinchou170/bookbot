def main():
    from stats.py import *


path = "books/frankenstein.txt"
text = get_book_text(path)
num_words = count_words(text)
lowered = lower_text(text)
frequency = count_characters(lowered)
freq = sort_by_frequency(frequency)

print(f"{num_words} words found in the document")
print(freq)

print(f"============ BOOKBOT ============\n Analyzing book found at {path}...\n ----------- Word Count ----------\n Found {num_words} total words\n --------- Character Count -------\n")
print()

if __name__ == "__main__":
    main()