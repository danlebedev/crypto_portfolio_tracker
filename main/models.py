from django.db import models


class Asset(models.Model):
    name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=10)

    class AssetTypes(models.IntegerChoices):
        STOCK = 1, 'stock'
        BOND = 2, 'bond'
        CURRENCY = 3, 'currency'
        COMMODITY = 4, 'commodity'
        CRYPTOCURRENCY = 5, 'cryptocurrency'

    asset_type = models.SmallIntegerField(
        choices=AssetTypes.choices,
        default=AssetTypes.CRYPTOCURRENCY,
    )

    def __str__(self):
        return self.short_name