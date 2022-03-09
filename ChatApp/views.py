from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render



def home_view(request):
    print(request)
    return render(request, "home.html")

