from django.shortcuts import render

# Create your views here.
from django.http impport HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
