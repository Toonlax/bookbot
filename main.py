def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def number_of_words(text_from_book):
    list_of_words = text_from_book.split()
    return len(list_of_words)

def main():
    result = get_book_text("books/frankenstein.txt")
    num_words = number_of_words(result)
    print(f"Found {num_words} total words")

main()