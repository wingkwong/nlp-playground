import nltk
from nltk.tokenize import sent_tokenize

text=""""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."""
tokenized_text=sent_tokenize(text)
print(tokenized_text)