import sys
from stats import get_num_words
from stats import get_num_occurrence
from stats import get_sorted_list



def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    text = get_book_text(filepath)
    count = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    char_dict = get_num_occurrence(text)
    sorted_list = get_sorted_list(char_dict)
    print("--------- Character Count -------")
    for dict in sorted_list:
        print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")

main()