#import from stats.py
from stats import get_book_wordcount
from stats import counting_characters
from stats import dictionary_sorter
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f: # do something with f (the file) here
        return f.read()

def main():
    print("Usage: python3 main.py <path_to_book")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    else:
        path_to_file = sys.argv[1] #"books/frankenstein.txt"
        book_text = get_book_text(path_to_file)
        number_of_words: int = get_book_wordcount(book_text)
        characters_counted = counting_characters(book_text)
        sorted_characters = dictionary_sorter(characters_counted)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_file}...")
        print("----------- Word Count ----------")
        print(f"Found {number_of_words} total words")
        print("--------- Character Count -------")
        for item in sorted_characters:
            char = item["char"]
            count = item["num"]
            if not char.isalpha():
                continue
            print(f"{char}: {count}")
        print("============= END ===============")

main() 





     