class CurrencyConverter:
    """
    This class handles currency conversion, allowing amounts to be converted between different currencies,
    retrieval of supported currencies, and management of currency rates.
    """

    def __init__(self):
        """
        Initialize currency rates based on the US dollar.
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

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        """
        Convert an amount from one currency to another.
        :param amount: float, The amount to convert.
        :param from_currency: str, The currency to convert from.
        :param to_currency: str, The currency to convert to.
        :return: float, The converted amount or False if an invalid currency is provided.
        """
        if from_currency not in self.rates or to_currency not in self.rates:
            return False
        
        # Convert the amount to USD, then to the target currency
        amount_in_usd = amount / self.rates[from_currency]
        converted_amount = amount_in_usd * self.rates[to_currency]
        return converted_amount

    def get_supported_currencies(self) -> list:
        """
        Get a list of supported currency types.
        :return: list, Supported currency types.
        """
        return list(self.rates.keys())

    def add_currency_rate(self, currency: str, rate: float) -> bool:
        """
        Add a new currency rate if the currency is not already supported.
        :param currency: str, The currency to add.
        :param rate: float, The exchange rate for the new currency.
        :return: bool, True if added successfully, False otherwise.
        """
        if currency in self.rates:
            return False
        self.rates[currency] = rate
        return True

    def update_currency_rate(self, currency: str, new_rate: float) -> bool:
        """
        Update the exchange rate for an existing currency.
        :param currency: str, The currency to update.
        :param new_rate: float, The new exchange rate.
        :return: bool, True if updated successfully, False otherwise.
        """
        if currency not in self.rates:
            return False
        self.rates[currency] = new_rate
        return True