import nltk
import sys

text_file = sys.argv[1]

with open(text_file, "r") as text:
    with open(text_file.replace("txt", "tok"), "w") as sink:
         for line in text:
             print(" ".join(nltk.word_tokenize(line)), file=sink)
