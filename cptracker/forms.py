from django.forms import ModelForm

from . import models


class PortfolioForm(ModelForm):
    class Meta:
        model = models.Portfolio
        fields = {'name'}