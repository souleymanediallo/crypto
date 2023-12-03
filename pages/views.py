import environ

from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

env = environ.Env()
api_key = env('CRYPTO_API_KEY')


# Create your views here.
def home(request):
    url = f"https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        context = {'data': data}
        return render(request, 'pages/index.html', context)
    return HttpResponse("Erreur : Impossible d'obtenir les taux de change.", status=500)


def search(request):
    if request.method == "POST":
        name_q = request.POST['name_q']
        url = f"https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.content)
            filtered_data = [article for article in data['Data'] if name_q in article['title'] or name_q in article['body']]
            context = {'data': filtered_data, 'name_q': name_q}
            print(data)
            return render(request, 'pages/search.html', context)
        return HttpResponse("Erreur : Impossible d'obtenir les taux de change.", status=500)
    else:
        notfound = "Veuillez saisir un nom de crypto-monnaie."
        context = {'notfound': notfound}
        return render(request, 'pages/search.html', context)


def price(request):
    quote = "BTC,ETH,XRP,BCH,LTC,ADA,DOGE,USDT,NEO,XLM"
    url = f"https://min-api.cryptocompare.com/data/pricemultifull?fsyms={quote}&tsyms=USD,EUR&api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        context = {'data': data}
        return render(request, 'pages/price.html', context)
    return HttpResponse("Erreur : Impossible d'obtenir les taux de change.", status=500)