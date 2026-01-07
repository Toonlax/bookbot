from stats import number_of_words, num_of_each_character, sorting

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    result = get_book_text("books/frankenstein.txt")
    num_words = number_of_words(result)
    num_character_dict = num_of_each_character(result)
    sorted_char_num = sorting(num_character_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print(sorted_char_num)
    print("============= END ===============")

main()