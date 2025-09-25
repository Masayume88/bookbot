from stats import word_count

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

main()