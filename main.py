from curses.ascii import isalpha
import sys
from stats import get_chars_count, get_sorted_dicts, get_words_count

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = args[1]
    content = get_book_text(path_to_book)
    num_words = get_words_count(content)
    chars_count = get_chars_count(content)
    list = get_sorted_dicts(chars_count)
    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main()
