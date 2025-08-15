from stats import get_num_words, get_chars_dict, sort_on
import sys

def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = get_chars_dict(text)

    #Printing report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sort_on(chars)
    print("============= END ===============")



def get_book_text(path):
    with open(path) as f:
        return f.read()
    

main()