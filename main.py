#tbd
def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    # Check ok. File contents from filepath parsed as string, output string.
    # print(text)
    num_words = word_count(text)
    print(f"Found {num_words} total words")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    word_list = text.split()
    word_count = 0

    for word in word_list:
        #Check ok. Are the words stored, sep whitespace, correctly.
        # print(word)
        word_count += 1
    
    return word_count

main()