def get_word_count(file_contents):
	word_count = len(str.split(file_contents))
	return word_count

def get_character_count(file_contents):
    char_list = []
    char_dict = {}
    for char in file_contents.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    sorted_char_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_char_dict