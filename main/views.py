from typing import Any, Dict
from django.db import models
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from . import models
from . import forms


def index(request):
    return render(request, 'main/index.html')

def assets(request):
    assets = models.Asset.objects.order_by('short_name')
    context = {
        'assets': assets,
    }
    return render(request, 'main/assets.html', context)

def asset(request, asset_id):
    asset = models.Asset.objects.get(id=asset_id)
    context = {'asset': asset}
    return render(request, 'main/asset.html', context)

class AssetUpdateView(UpdateView):
    model = models.Asset
    template_name = 'main/change_asset.html'
    form_class = forms.AssetForm
    success_url = reverse_lazy('main:assets')

    def get_context_data(self, *args, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['assets'] = models.Asset.objects.all()
        return context

class AssetCreateView(CreateView):
    template_name = 'main/add_asset.html'
    form_class = forms.AssetForm
    success_url = reverse_lazy('main:index')