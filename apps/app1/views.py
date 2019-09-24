from django.shortcuts import render, redirect
import requests
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

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

def contactview(request):
    name=''
    email=''
    comment=''


    form= ContactForm(request.POST or None)
    if form.is_valid():
        name= form.cleaned_data.get("name")
        email= form.cleaned_data.get("email")
        comment=form.cleaned_data.get("comment")

        if request.user.is_authenticated():
            subject= str(request.user) + "'s Comment"
        else:
            subject= "A Visitor's Comment"


        comment= name + " with the email, " + email + ", sent the following message:\n\n" + comment
        send_mail(subject, comment, settings.EMAIL_HOST_USER, ['vsecure4@gmail.com'])


        context= {'form': form}
        # return
        render(request, 'app1/contact.html', context)
        return redirect("/contact")

    else:
        context= {'form': form}
        return render(request, 'app1/contact.html', context)