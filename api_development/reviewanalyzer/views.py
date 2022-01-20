from django.shortcuts import render
from .apps import ReviewanalyzerConfig
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from tensorflow.keras.preprocessing.sequence import pad_sequences
from rest_framework import status

class ReviewView(APIView):
    def post(self, request):
        try:
            if len(request.data.keys())>1:
                return Response("Sorry, the request body should have one item at a time", status.HTTP_400_BAD_REQUEST)

            if "text" in request.data.keys():
                text =request.data['text']
                if len(text) == 0:
                    return Response("Invalid text(There must be at least one character!)", status=400)
                vector = ReviewanalyzerConfig.vectorizer.transform([text])
                prediction = ReviewanalyzerConfig.model_sentiment.predict(vector)[0]

                return JsonResponse({"text_sentiment": prediction}, status=200)

            elif "review" in request.data.keys():
                review =request.data['review']
                if len(review.strip()) == 0:
                    return Response("Invalid review(There must be at least one character!)", status=400)
                #For accurate tokenization
                review = [review]
                token = ReviewanalyzerConfig.tokenizer.texts_to_sequences(review)
                token = pad_sequences(token, maxlen= ReviewanalyzerConfig.max_len)

                prediction = (ReviewanalyzerConfig.model_spam().predict(token) >= 0.5).astype(int)[0][0]
                if prediction == 0:
                    prediction = 'Real'
                elif prediction == 1:
                    prediction = 'Spam'
                else:
                    pass

                return JsonResponse({"review_status": prediction}, status=200)

            else:
                pass

        except ValueError as e:
            return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


