def word_count(text):
    word_list = text.split()
    word_count = 0

    for word in word_list:
        #Check ok. Are the words stored, sep whitespace, correctly.
        # print(word)
        word_count += 1
    
    return word_count

def character_count(text):
    character_string = text.lower()
    character_dict = {}

    for character in character_string:
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1
    
    return character_dict

def sort_on(item):
    return item["num"]

def sorted_character_count(character_dict):
    sorted_character_list = []

    for ch, count in character_dict.items():
        if ch.isalpha():
            entry = {"char": ch, "num": count}
            sorted_character_list.append(entry)
    
    return sorted(sorted_character_list, reverse=True, key=sort_on)



