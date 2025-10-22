def get_book_text():
    with open("books/frankenstein.txt", "r") as f:
        text = f.read()
    return text

def word_count():
    book_text = get_book_text()
    words = book_text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")

def character_count():
    book_text = get_book_text().lower()
    characters = {}

    for c in book_text:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters

def stats():
    word_count()
    character_count()

stats()
