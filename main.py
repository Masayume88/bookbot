from stats import word_count, character_count, sorted_character_count
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_file = sys.argv[1]


    text = get_book_text(path_to_file)
    num_words = word_count(text)
    num_characters = character_count(text)
    sorted_num_characters = sorted_character_count(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_num_characters:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()