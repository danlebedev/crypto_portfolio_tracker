from django.shortcuts import render
from django.views.generic.edit import CreateView
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

class AssetCreateView(CreateView):
    template_name = 'main/add_asset.html'
    form_class = forms.AssetForm
    success_url = reverse_lazy('main:index')