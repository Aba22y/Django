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
        return HttpResponse(challenge)
    except:
        return HttpResponseNotFound("Type in a three letter month")
