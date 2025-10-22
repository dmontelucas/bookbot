def get_book_text():
    with open("books/frankenstein.txt", "r") as f:
        text = f.read()
    return text


#def print_book():
    #book_text = get_book_text()
    #print(book_text)

def main():
    from stats import word_count
    #print_book()

main()
