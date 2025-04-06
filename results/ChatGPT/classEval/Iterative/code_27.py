class CurrencyConverter:
    """
    A class for currency conversion that supports converting amounts between different currencies,
    retrieving supported currencies, adding new currency rates, and updating existing currency rates.
    """

    def __init__(self):
        """
        Initialize the exchange rates of various currencies against the US dollar.
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
        Convert an amount from one currency to another.

        :param amount: float, The amount of the source currency.
        :param from_currency: str, The source currency type.
        :param to_currency: str, The target currency type.
        :return: float, The amount converted to the target currency.
        :raises ValueError: If either currency is not supported.
        """
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError("Unsupported currency")

        # Convert amount to USD first
        amount_in_usd = amount / self.rates[from_currency]
        # Convert USD to target currency
        converted_amount = amount_in_usd * self.rates[to_currency]
        return converted_amount

    def get_supported_currencies(self):
        """
        Returns a list of supported currency types.

        :return: list, All supported currency types.
        """
        return list(self.rates.keys())

    def add_currency_rate(self, currency, rate):
        """
        Add a new supported currency type.

        :param currency: str, The currency type to be added.
        :param rate: float, The exchange rate for this currency type.
        :return: None if successful, False if unsuccessful.
        """
        if currency in self.rates:
            return False
        self.rates[currency] = rate
        return None

    def update_currency_rate(self, currency, new_rate):
        """
        Update the exchange rate for a specific currency.

        :param currency: str, The currency type.
        :param new_rate: float, The new exchange rate.
        :return: None if successful, False if unsuccessful.
        """
        if currency not in self.rates:
            return False
        self.rates[currency] = new_rate
        return None