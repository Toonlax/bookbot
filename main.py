from stats import number_of_words, num_of_each_character

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    result = get_book_text("books/frankenstein.txt")
    num_words = number_of_words(result)
    num_character_dict = num_of_each_character(result)

    print(f"Found {num_words} total words")
    print(num_character_dict)

main()