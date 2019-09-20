from django.shortcuts import render, redirect
import requests

# Create your views here.

def index(request):

    url = 'https://www.virustotal.com/vtapi/v2/url/scan' #Scan the URL

    params = {'apikey': '6c72dc928ae0eb65656cbdc4a9898ba4b8ba8073acdcb45659911648640b5fd4', 'url':'www.google.com'}

    response = requests.post(url, data=params)

    print(response.json())

    url2 = 'https://www.virustotal.com/vtapi/v2/url/report' #Retrieve URL scan report

    params2 = {'apikey': '6c72dc928ae0eb65656cbdc4a9898ba4b8ba8073acdcb45659911648640b5fd4', 'resource':response.json()['scan_id']}

    response2 = requests.get(url2, params=params2)

    print(response2.json())

    return redirect("/")