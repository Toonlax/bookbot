# Imports ====================================================================
from stats import count_words, count_characters, get_sorted_letter_counts
import sys

# Reads the file at path and returns its contents as a string
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

# Main logic flow  ===========================================================
def main():
    book_text = get_book_text(sys.argv[1])
    word_count = count_words(book_text)
    char_counts = count_characters(book_text)
    sorted_char_counts = get_sorted_letter_counts(char_counts)

    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_char_counts:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

# Execution logic ============================================================
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main()