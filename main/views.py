from django.shortcuts import render

from . import models


def index(request):
    asset = models.Asset.objects.order_by('short_name')
    context = {'asset': asset}
    return render(request, 'main/index.html', context)