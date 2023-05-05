from django.db import models


class Portfolio(models.Model):
    name = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=24, decimal_places=12)
    created = models.DateTimeField(auto_now_add=True, db_index=True)