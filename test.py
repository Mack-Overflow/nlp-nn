# import nltk
# nltk.download('stopwords')
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer, LancasterStemmer

# tweet = """Hello there guys! It's amazing how impressive the @huggingface model is!"""
# tweet = tweet.lower().split()
# stop_words = stopwords.words('english')
# stop_words = set(stop_words)
# tweet_no_stop = [word for word in tweet if word not in stop_words]
# chars = [char for char in tweet_no_stop]

# text2 = "I am amazed by how amazingly amazing you are."
# words_to_stem = ['happy', 'happier', 'cactus', 'cactii', 'elephant', 'elephants', 'amazed', 'amazingly', 'amazing']

# porter = PorterStemmer()
# lancaster = LancasterStemmer()

# stemmed = [(porter.stem(word), lancaster.stem(word)) for word in words_to_stem]
import nltk
# nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
words = ['tremble', 'trembling', 'trembler', 'trembled']

# print(stemmed)
# print(stop_words[:10])