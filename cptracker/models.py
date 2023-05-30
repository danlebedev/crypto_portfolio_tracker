from django.db import models

from main.models import Asset


class Portfolio(models.Model):
    name = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True, db_index=True)

class UserAsset(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=24, decimal_places=12)