class CurrencyConverter:
    """
    This is a class for currency conversion, which supports to convert amounts between different currencies, retrieve supported currencies, add new currency rates, and update existing currency rates.
    """

    def __init__(self, rates=None):
        """
        Initialize the exchange rate of the US dollar against various currencies
        """
        if rates is None:
            self.rates = {
                'USD': 1.0,
                'EUR': 0.85,
                'GBP': 0.72,
                'JPY': 110.15,
                'CAD': 1.23,
                'AUD': 1.34,
                'CNY': 6.40,
            }
        else:
            self.rates = rates

    def convert(self, amount, from_currency, to_currency):
        """
        Convert the value of a given currency to another currency type
        :param amount: float, The value of a given currency
        :param from_currency: string, source currency type
        :param to_currency: string, target currency type
        :return: float, value converted to another currency type
        :raises ValueError: if from_currency or to_currency is not supported.
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number (int or float)")

        if not isinstance(from_currency, str) or not isinstance(to_currency, str):
            raise TypeError("Currency codes must be strings")

        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in self.rates:
            raise ValueError(f"Currency '{from_currency}' not supported.")
        if to_currency not in self.rates:
            raise ValueError(f"Currency '{to_currency}' not supported.")

        usd_amount = amount / self.rates[from_currency]
        converted_amount = usd_amount * self.rates[to_currency]
        return round(converted_amount, 2)

    def get_supported_currencies(self):
        """
        Returns a list of supported currency types
        :return: list, All supported currency types
        """
        return list(self.rates.keys())

    def add_currency_rate(self, currency, rate):
        """
        Add a new supported currency type
        :param currency: string, currency type to be added
        :param rate: float, exchange rate for this type of currency
        :raises TypeError: if currency is not a string or rate is not a number.
        :raises ValueError: if currency already exists.
        """

        if not isinstance(currency, str):
            raise TypeError("Currency must be a string.")
        if not isinstance(rate, (int, float)):
            raise TypeError("Rate must be a number (int or float).")

        currency = currency.upper()

        if currency in self.rates:
            raise ValueError(f"Currency '{currency}' already exists.")

        self.rates[currency] = rate

    def update_currency_rate(self, currency, new_rate):
        """
        Update the exchange rate for a certain currency
        :param currency: string
        :param new_rate: float
        :raises TypeError: if currency is not a string or new_rate is not a number.
        :raises ValueError: if currency does not exist.
        """
        if not isinstance(currency, str):
            raise TypeError("Currency must be a string.")
        if not isinstance(new_rate, (int, float)):
            raise TypeError("New rate must be a number (int or float).")

        currency = currency.upper()

        if currency not in self.rates:
            raise ValueError(f"Currency '{currency}' not found.")

        self.rates[currency] = new_rate