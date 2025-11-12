from stats import get_count_of_words, get_count_of_characters, make_list_from_dict, sort_on
import sys

def get_book_text (path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_book = get_book_text(sys.argv[1]) 
        print("============ BOOKBOT ============")
        print("Analyzing book found at ")
        print("----------- Word Count ----------")
        print(f"Found {get_count_of_words(path_to_book)} total words")
        print("--------- Character Count -------")
        counts_list = make_list_from_dict(path_to_book)
        counts_list.sort(reverse=True, key=sort_on)
        for entry in counts_list:
            ch = entry["char"]
            if not ch.isalpha():
                continue
            print(f"{ch}: {entry['num']}")
        print("============= END ===============")
if __name__ == '__main__':
    main()