from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'shopping/index.html')

def store(request):
    return render(request, 'shopping/store.html')