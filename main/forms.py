from django.forms import ModelForm

from . import models


class AssetForm(ModelForm):
    class Meta:
        model = models.Asset
        fields = ('name', 'short_name', 'asset_type')