from django.db import models
from django.core.validators import MinValueValidator
import datetime

class Account(models.Model):
    amount = models.FloatField(default=0)
    user = models.ForeignKey('authapp.User', on_delete=models.DO_NOTHING, null=True)
    REQUIRED_FIELDS = ['amount', 'user']


class CurrencyRates(models.Model):
    RUB = models.FloatField(null=True)
    EUR = models.FloatField(null=True)
    USD = models.FloatField(null=True)
    date = models.DateField(null=True)
    REQUIRED_FIELDS = ['RUB', 'EUR', 'USD',]


class Category(models.Model):
    name = models.CharField(null=True, max_length=255)
    limit = models.DecimalField(decimal_places=2, max_digits=12) #, validators=[MinValueValidator(Decimal('0.01'))]
    REQUIRED_FIELDS = ['name', 'limit',]


class AccountHistory(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=12) #, validators=[MinValueValidator(Decimal('0.01'))]
    date = models.DateField(null=True, default=datetime.date.today)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='history')
    type = models.IntegerField()
    description = models.TextField()
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, null=True)
    REQUIRED_FIELDS = ['amount', 'type',]