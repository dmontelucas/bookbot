def get_book_text():
    with open("books/frankenstein.txt", "r") as f:
        text = f.read()
    return text

def word_count():
    book_text = get_book_text()
    words = book_text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")

def stats():
    word_count()

stats()
