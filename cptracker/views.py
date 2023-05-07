from django.shortcuts import render

from . import models


def index(request):
    return render(request, 'cptracker/index.html')

def portfolios(request):
    """Extracts all portfolio records from the database."""
    portfolios =  models.Portfolio.objects.order_by('name')
    context = {'portfolios': portfolios}
    return render(request, 'cptracker/portfolios.html', context)

def portfolio(request, portfolio_id):
    portfolio = models.Portfolio.objects.get(id=portfolio_id)
    context = {'portfolio': portfolio}
    return render(request, 'cptracker/portfolio.html', context)
