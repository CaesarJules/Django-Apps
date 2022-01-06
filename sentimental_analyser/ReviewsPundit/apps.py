from django.apps import AppConfig
from django.conf import settings
import os
import pickle


class ReviewspunditConfig(AppConfig):
    name = 'ReviewsPundit'

    path = os.path.join(settings.MODELS, 'model.p')

    with open(path, 'rb') as p:
        data = pickle.load(p)
    model = data['model']
    vectorizer = data['vectorizer']

