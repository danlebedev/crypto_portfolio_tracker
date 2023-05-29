from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
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

class PortfolioUpdateView(UpdateView):
    model = models.Portfolio
    template_name = 'cptracker/change_portfolio.html'
    form_class = forms.PortfolioForm
    success_url = reverse_lazy('cptracker:portfolios')

    def get_context_data(self, *args, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['assets'] = models.Portfolio.objects.all()
        return context

class PortfolioCreateView(CreateView):
    template_name = 'cptracker/add_portfolio.html'
    form_class = forms.PortfolioForm
    success_url = reverse_lazy('cptracker:portfolios')