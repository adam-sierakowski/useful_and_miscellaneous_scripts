from collections import Counter
import re

input_filename = "my_corpus.txt"
output_filename = input_filename.split(".")[0] + "_wordcount.txt"

words = []

with open(input_filename, "r", encoding="utf-8") as f:
	for line in f:
		line = re.sub(r"([\.,…:;\*„”\?\!])", r" \1 ", line)
		line = line.replace("  ", " ").strip()
		tokenized_line = re.split(r'[ \b\n]', line)
		words.extend(list(tokenized_line))

counted_words = Counter(words)

def sort_dict(unsorted_dict):
	sorted_dict = dict(sorted(unsorted_dict.items(), key = lambda x: x[1], reverse = True))
	return sorted_dict

counted_words = sort_dict(counted_words)

with open(output_filename, "w", encoding="utf-8") as f:
	for word, count in counted_words.items():
		if word != "\n" and word != "\t":
			print(f"{word}\t{count}", file = f)
	print(f"Output saved to {output_filename}")

