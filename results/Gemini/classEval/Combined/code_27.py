class CurrencyConverter:
    """
    This is a class for currency conversion, which supports to convert amounts between different currencies, retrieve supported currencies, add new currency rates, and update existing currency rates.
    """

    def __init__(self):
        """
        Initialize the exchange rate of the US dollar against various currencies
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
        Convert the value of a given currency to another currency type
        :param amount: float, The value of a given currency
        :param from_currency: string, source currency type
        :param to_currency: string, target currency type
        :return: float, value converted to another currency type
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")
        if not isinstance(from_currency, str) or not isinstance(to_currency, str):
            raise TypeError("Currencies must be strings.")

        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in self.rates or to_currency not in self.rates:
            return False

        from_rate = self.rates[from_currency]
        to_rate = self.rates[to_currency]

        usd_amount = amount / from_rate
        converted_amount = usd_amount * to_rate

        return converted_amount

    def get_supported_currencies(self):
        """
        Returns a list of supported currency types
        :return:list, All supported currency types
        """
        return list(self.rates.keys())

    def add_currency_rate(self, currency, rate):
        """
        Add a new supported currency type, return False if the currency type is already in the support list
        :param currency:string, currency type to be added
        :param rate:float, exchange rate for this type of currency
        :return:If successful, returns None; if unsuccessful, returns False
        """
        if not isinstance(currency, str):
            raise TypeError("Currency must be a string.")
        if not isinstance(rate, (int, float)):
            raise TypeError("Rate must be a number.")

        currency = currency.upper()

        if currency in self.rates:
            return False

        self.rates[currency] = rate
        return None

    def update_currency_rate(self, currency, new_rate):
        """
        Update the exchange rate for a certain currency
        :param currency:string
        :param new_rate:float
        :return:If successful, returns None; if unsuccessful, returns False
        """
        if not isinstance(currency, str):
            raise TypeError("Currency must be a string.")
        if not isinstance(new_rate, (int, float)):
            raise TypeError("New rate must be a number.")

        currency = currency.upper()

        if currency not in self.rates:
            return False

        self.rates[currency] = new_rate
        return None