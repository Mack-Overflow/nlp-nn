# import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
tweet = """Hello there guys! It's amazing how impressive the @huggingface model is!"""
tweet = tweet.lower().split()
stop_words = stopwords.words('english')
stop_words = set(stop_words)
tweet_no_stop = [word for word in tweet if word not in stop_words]
chars = [char for char in tweet_no_stop]


print(chars)
# print(stop_words[:10])