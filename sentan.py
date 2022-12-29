import flair

# model = flair.models.TextClassifier.load("en-sentiment")

# # text = "GBP Rallies after stronger than ever economic performance"
text = "GBP slips on fears of a divided economy"
# sentence = flair.data.Sentence(text)

# model.predict(sentence)
# print(sentence.get_labels()[0].score)

"""
Sentiment Analysis models (BERT)

Padding tokens:
CLS: 101
SEP: 102
MASK: 103
UNK: 100
PAD: 0
"""
model_name = 'ProsusAI/finbert'
from transformers import BertForSequenceClassification
from transformers import BertTokenizer

model = BertForSequenceClassification.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)
tokens = tokenizer.encode_plus(text, max_length=512, truncation=True, padding='max_length', add_special_tokens=True, return_tensors='pt')
print(tokens)