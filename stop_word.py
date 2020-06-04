import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

text=""""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."""
tokenized_sent=sent_tokenize(text)
# print(tokenized_word)
stop_words=set(stopwords.words("english"))
print(stop_words)
# -------------------------
# Removing stopwords
# -------------------------
filtered_sent=[]
for w in tokenized_sent:
    if w not in stop_words:
        filtered_sent.append(w)
print("Tokenized Sentence:",tokenized_sent)
print("Filterd Sentence:",filtered_sent)