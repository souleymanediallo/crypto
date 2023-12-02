from django.shortcuts import render
from django.http import HttpResponse
import requests
import json


# Create your views here.
def home(request):
    url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        context = {'data': data}
        return render(request, 'pages/index.html', context)
    return HttpResponse("Erreur : Impossible d'obtenir les taux de change.", status=500)