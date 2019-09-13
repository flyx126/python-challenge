import os
import csv
import re

pyparagraph = os.path.join(".","Paragraph.txt")


with open(pyparagraph,"r",encoding = "UTF-8") as Paragraph:
    reader = Paragraph.read()
    sentences_sep = re.sub('\n', '', reader)
    sentences_split = re.split('\.', sentences_sep)

    letters_sep = re.sub("[\., \-')()><\n]", '', reader).replace('"', '')
    letters = list(letters_sep)

    words_sep = re.sub("[\.,\-')()><\n]", '', reader).replace('"', '')
    words_split = re.split(' ', words_sep)

print("\nParagraph Analysis")
print("----------------------------")
print("Approximate Word Count:", len(words_split))
print("Approximate Sentence Count:", len(sentences_split) - 1)
print("Average Letter Count:", round(len(letters_sep) / len(words_split), 4), "per word")
print("Average Sentence Length:", round(len(words_split) / (len(sentences_split) - 1), 4), "words")
print("\n")