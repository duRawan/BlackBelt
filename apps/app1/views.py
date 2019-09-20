from django.shortcuts import render
import requests

# Create your views here.
#test

def index(request):
    
    url = 'https://www.virustotal.com/vtapi/v2/url/scan'

    params = {'apikey': '6c72dc928ae0eb65656cbdc4a9898ba4b8ba8073acdcb45659911648640b5fd4', 'url':'www.google.com'}

    response = requests.post(url, data=params)

    print(response.json())