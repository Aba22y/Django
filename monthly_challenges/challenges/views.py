from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge(req, month):
    challenge_text = None
    if month == "jan":
        challenge_text = "first day of da month"
    elif month == "feb":
        challenge_text = "second day of da month"
    else:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)