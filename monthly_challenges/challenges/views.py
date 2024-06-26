from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

months = {
    "jan": "run",
    "feb": "jump",
    "mar": "swim",
    "apr": "walk",
    "may": "code",
    "jun": "sleep",
    "jul": "reflect",
    "aug": "eat",
    "sep": "sing",
    "oct": "lament",
    "nov": "django",
    "dec": "gym"
}

# Create your views here.

def index(req):
    listItems = ""
    for month in list(months.keys()):
        url = reverse("month-challenge", args=[month])
        listItems += f"<li><a href=\"{url}\">{month.capitalize()}</a></li>"
    htmlList = f"<ul>{listItems}</ul>"
    return HttpResponse(htmlList)

def monthly_challenge_numbers(req, month):
    monthList = list(months.keys())
    if month > len(monthList) or month < 1:
        return HttpResponseNotFound("Invalid month")
    redirect = monthList[month-1]
    #this is a dynamic way to generate the url instead of hard coding /challenges/
    redirectPath = reverse("month-challenge", args=[redirect])
    return HttpResponseRedirect(redirectPath)

def monthly_challenge(req, month):
    try:
        challenge = months[month]
        responseHTML = f"<h1>{challenge}</h1>"
        return HttpResponse(responseHTML)
    except:
        return HttpResponseNotFound("<h1>Type in a three letter month</h1>")
