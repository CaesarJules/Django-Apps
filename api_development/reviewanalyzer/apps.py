from django.apps import AppConfig
from django.conf import settings
import os
import pickle


class ReviewanalyzerConfig(AppConfig):
    name = 'reviewanalyzer'

    path_sentiment = os.path.join(settings.MODELS, 'model.p')
    path_spam = os.path.join(settings.MODELS, 'spam_classifier.p')

    with open(path_sentiment, 'rb') as p:
        data = pickle.load(p)
    model_sentiment = data['model']
    vectorizer = data['vectorizer']

    with open(path_spam, 'rb') as p:
        data = pickle.load(p)
    model_spam = data['model']
    tokenizer = data['tokenizer']
    max_len = data['maxlen']



