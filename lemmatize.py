import nltk
# nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
words = ['tremble', 'trembling', 'trembler', 'trembled']

lemmatizer = WordNetLemmatizer()
print([lemmatizer.lemmatize(word, wordnet.VERB) for word in words])
