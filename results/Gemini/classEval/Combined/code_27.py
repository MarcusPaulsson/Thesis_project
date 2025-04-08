class CurrencyConverter:
    """
    This is a class for currency conversion, which supports to convert amounts between different currencies,
    retrieve supported currencies, add new currency rates, and update existing currency rates.
    """

    def __init__(self):
        """
        Initialize the exchange rate of the US dollar against various currencies.
        Rates are stored as a USD equivalent.
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

        :param amount: float, The value of a given currency.
        :param from_currency: str, Source currency type.
        :param to_currency: str, Target currency type.
        :return: float, Value converted to another currency type, or False if conversion is not possible.
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")
        if not isinstance(from_currency, str) or not isinstance(to_currency, str):
            raise TypeError("Currencies must be strings.")

        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in self.rates or to_currency not in self.rates:
            return False

        try:
            from_rate = self.rates[from_currency]
            to_rate = self.rates[to_currency]

            usd_amount = amount / from_rate
            converted_amount = usd_amount * to_rate

            return converted_amount
        except ZeroDivisionError:
            return False  # Handle potential division by zero

    def get_supported_currencies(self):
        """
        Returns a list of supported currency codes.

        :return: list, All supported currency codes.
        """
        return list(self.rates.keys())

    def add_currency_rate(self, currency, rate):
        """
        Add a new supported currency type.

        :param currency: str, Currency code to be added.
        :param rate: float, Exchange rate for this currency (relative to USD).
        :return: True if successful, False if the currency already exists or if rate is invalid.
        """
        if not isinstance(currency, str):
            raise TypeError("Currency must be a string.")
        if not isinstance(rate, (int, float)):
            raise TypeError("Rate must be a number.")

        currency = currency.upper()

        if currency in self.rates:
            return False

        if rate <= 0:
            return False  # Rate must be positive

        self.rates[currency] = rate
        return True

    def update_currency_rate(self, currency, new_rate):
        """
        Update the exchange rate for a certain currency.

        :param currency: str, Currency code to update.
        :param new_rate: float, New exchange rate (relative to USD).
        :return: True if successful, False if the currency doesn't exist or if rate is invalid.
        """
        if not isinstance(currency, str):
            raise TypeError("Currency must be a string.")
        if not isinstance(new_rate, (int, float)):
            raise TypeError("Rate must be a number.")

        currency = currency.upper()

        if currency not in self.rates:
            return False

        if new_rate <= 0:
            return False  # Rate must be positive

        self.rates[currency] = new_rate
        return True


if __name__ == '__main__':
    import doctest

    doctest.testmod()