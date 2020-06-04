import nltk
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

text=""""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."""
tokenized_word=word_tokenize(text)
# print(tokenized_word)
fdist = FreqDist(tokenized_word)
print(fdist)
fdist.most_common(2)
fdist.plot(30,cumulative=False)
plt.show()