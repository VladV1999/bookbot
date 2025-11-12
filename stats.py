def get_count_of_words(text):
    text_list = text.split()
    return len(text_list)

def get_count_of_characters(count_of_words):
    character_dictionary = {}
    for char in count_of_words:
        char = char.lower()
        character_dictionary[char] = character_dictionary.get(char, 0) + 1

    return character_dictionary

def make_list_from_dict(count_of_words):
    result = []
    dictionary = get_count_of_characters(count_of_words)
    for c,n in dictionary.items():
        result.append({"char": c, "num": n})
    return result

def sort_on(item):
    return item["num"]
