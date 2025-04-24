class CurrencyConverter:
    """
    A class for currency conversion, supporting conversion between different currencies,
    retrieving supported currencies, adding new currency rates, and updating existing currency rates.
    """

    def __init__(self):
        """
        Initialize the exchange rates for various currencies against the US dollar.
        """
        self.rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.72,
            'JPY': 110.15,
            'CAD': 1.23,
            'AUD': 1.34,
            'CNY': 6.40,
        }

    def convert(self, amount, from_currency, to_currency):
        """
        Convert the value of a given currency to another currency type.

        :param amount: float, The value of a given currency
        :param from_currency: string, source currency type
        :param to_currency: string, target currency type
        :return: float, value converted to another currency type or False if currencies are unsupported
        """
        if from_currency not in self.rates or to_currency not in self.rates:
            return False

        # Convert amount to USD first
        amount_in_usd = amount / self.rates[from_currency]
        # Convert USD to the target currency
        converted_amount = amount_in_usd * self.rates[to_currency]
        return converted_amount

    def get_supported_currencies(self):
        """
        Returns a list of supported currency types.

        :return: list, All supported currency types
        """
        return list(self.rates.keys())

    def add_currency_rate(self, currency, rate):
        """
        Add a new supported currency type. Return False if the currency type is already in the support list.

        :param currency: string, currency type to be added
        :param rate: float, exchange rate for this type of currency
        :return: None if successful; False if unsuccessful
        """
        if currency in self.rates:
            return False
        self.rates[currency] = rate

    def update_currency_rate(self, currency, new_rate):
        """
        Update the exchange rate for a certain currency.

        :param currency: string
        :param new_rate: float
        :return: None if successful; False if unsuccessful
        """
        if currency not in self.rates:
            return False
        self.rates[currency] = new_rate