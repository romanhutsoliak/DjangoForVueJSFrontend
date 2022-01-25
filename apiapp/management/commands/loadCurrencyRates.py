from django.core.management.base import BaseCommand, CommandError
from django.http.request import HttpRequest
import requests, json
from ...models import CurrencyRates
from datetime import datetime

class Command(BaseCommand):
    help = 'python manage.py loadCurrencyRates 2021-11-28'

    def add_arguments(self, parser):
        parser.add_argument('date', help='Currency date', nargs='?')

    def handle(self, *args, **options):

        response = requests.get('http://www.floatrates.com/daily/rub.json')
        response.raise_for_status()  # raises exception when not a 2xx response
        if response.status_code != 204:
            json_data = json.loads(response.text)

            currencyRates = CurrencyRates.objects.get(id=1)
            currencyRates.RUB = 1
            currencyRates.EUR = 1/json_data['eur']['rate']
            currencyRates.USD = 1/json_data['usd']['rate']
            currencyRates.date = options['date'] if options['date'] else datetime.now().strftime("%Y-%m-%d")
            currencyRates.save()

            self.stdout.write(self.style.SUCCESS('Currency rates has been updated "%s"' % currencyRates.date))



        
        