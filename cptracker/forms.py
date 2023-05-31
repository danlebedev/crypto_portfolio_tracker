from django.forms import ModelForm, ModelChoiceField

from . import models


class PortfolioForm(ModelForm):
    class Meta:
        model = models.Portfolio
        fields = ('name',)

class UserAssetForm(ModelForm):
    class Meta:
        model = models.UserAsset
        fields = ('asset', 'balance',)
        field_classes = {'asset': ModelChoiceField}