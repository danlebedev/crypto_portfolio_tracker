from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from . import models
from . import forms


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

class PortfolioCreateView(CreateView):
    template_name = 'cptracker/add_portfolio.html'
    form_class = forms.PortfolioForm
    success_url = reverse_lazy('cptracker:portfolios')