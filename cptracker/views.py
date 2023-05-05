from django.shortcuts import render

def index(request):
    return render(request, 'cptracker/index.html')