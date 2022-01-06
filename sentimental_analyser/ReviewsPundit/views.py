from django.shortcuts import render
from .apps import ReviewspunditConfig
from django.http import JsonResponse
from rest_framework.views import APIView

class call_model(APIView):
    def get(self, request):
        if request.method == 'GET':
            #Retrieve the input sentence
            text = request.GET.get('text')
            #Vectorize the document
            vector = ReviewspunditConfig.vectorizer.transform([text])
            prediction = ReviewspunditConfig.model.predict(vector)[0]

            return JsonResponse({'text_sentiment': prediction})
