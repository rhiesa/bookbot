from stats import get_word_count
from stats import get_character_count
import sys

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return (file_contents)

def main():
	#check for sys inputs
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	#read book texts
	file_contents = get_book_text(sys.argv[1])	
	word_count = get_word_count(file_contents)
	char_list = get_character_count(file_contents)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at /books/frankenstein.txt...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("----------- Character Count ----------")
	for char, count in char_list.items():
		if char.isalpha():
  			print(f"{char}: {count}")
	print("=================================")
	print("============= END ===============")
main()
