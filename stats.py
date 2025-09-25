def word_count(text):
    word_list = text.split()
    word_count = 0

    for word in word_list:
        #Check ok. Are the words stored, sep whitespace, correctly.
        # print(word)
        word_count += 1
    
    return word_count