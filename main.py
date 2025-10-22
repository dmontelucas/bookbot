import sys
from stats import word_count, character_count

def get_book_text(filename):
    script_dir = sys.path[0]
    
    book_path = script_dir + "/" + filename
    with open(book_path, "r") as f:
        text = f.read()
    return text


#def print_book():
    #book_text = get_book_text()
    #print(book_text)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filename = sys.argv[1]
    book_text = get_book_text(filename)
    num_words = word_count(book_text)
    print(f"Found {num_words} total words")

    char_dict = character_count(book_text)
    for ch, count in sorted(char_dict.items()):
        print(f"{ch}: {count}")
    


main()
