from collections import Counter
from unicodedata import name

chars = []
with open ("my_corpus.txt", "r", encoding="utf-8") as f:
	for line in f:
		chars.extend(list(line))

counted_chars = Counter(chars)

def sort_dict(unsorted_dict):
	sorted_dict = dict(sorted(unsorted_dict.items(), key = lambda x: x[1], reverse = True))
	return sorted_dict

counted_chars = sort_dict(counted_chars)

for character, count in counted_chars.items():
	if character != "\n" and character != "\t":
		print(f"{character}\t{count}\t{str(hex(ord(character)))}\t{name(character)}")
	else:
		print(f"{repr(character)}\t{count}\t{str(hex(ord(character)))}")

