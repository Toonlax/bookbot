def number_of_words(text_from_book):
    list_of_words = text_from_book.split()
    return len(list_of_words)

def num_of_each_character(text):
    character_count_dict = {}
    for t in text:
        lower_char = t.lower()
        if lower_char in character_count_dict:
            character_count_dict[lower_char] += 1
        else:
            character_count_dict[lower_char] = 1
    return character_count_dict