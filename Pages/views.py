from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'Pages/index.html')

def about(request):
    return render(request, 'Pages/about.html')


