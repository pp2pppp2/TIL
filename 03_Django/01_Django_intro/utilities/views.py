from django.shortcuts import render
from decouple import config
import requests
import json

# Create your views here.
def index(request):
    return render(request, 'utilities/index.html')

# NAVER MAMAGO 번역

def mamago(request):
    return render(request, 'utilities/mamago.html')

def translated(request):
    word = request.GET.get('word')
    
    naver_client_id = config('NAVER_CLIENT_ID')
    naver_client_secret = config('NAVER_CLIENT_SECRET')

    mamago_url = 'https://openapi.naver.com/v1/papago/n2mt'

    header = {
        'X-Naver-Client-Id':naver_client_id,
        'X-Naver-Client-Secret' : naver_client_secret,
    }

    data = {
        'source' : 'ko',
        'target' : 'en',
        'text' : word,
    }
    result = requests.post(mamago_url , headers=header, data=data).json()

    tr_word = result.get('message').get('result').get('translatedText')

    context = {
        'word' : word,
        'tr_word' : tr_word,
    }

    return render(request, 'utilities/translated.html', context)