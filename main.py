from stats import number_of_words, wie_oft, sorted_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as book:
        file_contents = book.read()
    return file_contents

def main():
    print(get_book_text("books/frankenstein.txt"))

path = sys.argv[1]
number_of_words(get_book_text(path))
#wie_oft_var = wie_oft(get_book_text(path))
#print(wie_oft_var)
#main()
result = sorted_dict(wie_oft(get_book_text(path)))

print("============ BOOKBOT ============")
print(f"Analyzing book found at {path}...")
print("----------- Word Count ----------")
print(f"Found {number_of_words(get_book_text(path))} total words")
print("--------- Character Count -------")
for i in range(0,len(result)):
    if result[i]["char"].isalpha():
        print(f"{result[i]["char"]}: {result[i]["num"]}")
        
print("============= END ===============")