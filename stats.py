# Gets the number of words within the book
def count_words(text_from_book):
    list_of_words = text_from_book.split()
    return len(list_of_words)

# Creates a dictionary whose items contain characters as key objects and the amount of times that character appears in the book as the value objects
def count_characters(book_string):
    character_and_count_dict = {}
    for char in book_string:
        lower_char = char.lower()
        if lower_char in character_and_count_dict:
            character_and_count_dict[lower_char] += 1
        else:
            character_and_count_dict[lower_char] = 1
    return character_and_count_dict

# Will be used to sort by the key "num"
def sort_on(items):
    return items["num"]
# Creates a list containing multiple dictionaires and then filters out anything that isn't an alphabetical character and sorts it by the biggest number on top.
def get_sorted_letter_counts(char_dict):
    list_of_dicts = []

    for key, value in char_dict.items():
        iteration_dict = {
            "char": key,
            "num": value
        }
        if iteration_dict["char"].isalpha():
            list_of_dicts.append(iteration_dict)

    list_of_dicts.sort(reverse = True, key = sort_on)
    return list_of_dicts

