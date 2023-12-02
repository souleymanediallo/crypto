#import os
#from dotenv import load_dotenv
import environ

from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# https://pypi.org/project/python-dotenv/
#load_dotenv()

env = environ.Env()

api_key = env('CRYPTO_API_KEY')
#api_key = os.getenv('CRYPTO_API_KEY')


# Create your views here.
def home(request):
    url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        context = {'data': data}
        return render(request, 'pages/index.html', context)
    return HttpResponse("Erreur : Impossible d'obtenir les taux de change.", status=500)


def price(request):
    quote = "BTC,ETH,XRP,BCH,LTC,ADA,DOGE,USDT,NEO,XLM"
    url = f"https://min-api.cryptocompare.com/data/pricemultifull?fsyms={quote}&tsyms=USD,EUR&api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        context = {'data': data}
        return render(request, 'pages/price.html', context)
    return HttpResponse("Erreur : Impossible d'obtenir les taux de change.", status=500)