import requests
import json
from config import keys


class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):

        if quote == base:
            raise APIException(f'Please, try again: currencies should not be identical. You entered two identical currencies: {base}.')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Please select currency from the list. You entered not existing currency: {base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Please select currency from the list. You entered not existing currency: {quote}')

        try:
            amount = float(amount)

        except ValueError:
            raise APIException(f'Currency amount should be digital or decimals. Use period for decimals. You entered not allowed amount:  {amount}')

        if amount < 0:
            raise APIException(f'Please try again: Currency quantity should not be negative')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_base = json.loads(r.content)[keys[quote]]
        total_base = total_base * amount

        return total_base
