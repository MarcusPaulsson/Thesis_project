class CurrencyConverter:
    """
    A class for currency conversion, supporting conversions between different currencies, 
    retrieval of supported currencies, addition of new currency rates, and updating existing currency rates.
    """

    def __init__(self):
        """Initialize the exchange rates for various currencies against the US dollar."""
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
        
        :param amount: The amount to convert.
        :param from_currency: The currency to convert from.
        :param to_currency: The currency to convert to.
        :return: The converted amount, or False if invalid currency.
        """
        if from_currency not in self.rates or to_currency not in self.rates:
            return False
        
        amount_in_usd = amount / self.rates[from_currency]
        converted_amount = amount_in_usd * self.rates[to_currency]
        return converted_amount

    def get_supported_currencies(self) -> list:
        """Return a list of supported currency types."""
        return list(self.rates.keys())

    def add_currency_rate(self, currency: str, rate: float) -> bool:
        """
        Add a new currency rate.
        
        :param currency: The currency to add.
        :param rate: The exchange rate for the new currency.
        :return: True if successfully added, False if the currency already exists.
        """
        if currency in self.rates:
            return False
        self.rates[currency] = rate
        return True

    def update_currency_rate(self, currency: str, new_rate: float) -> bool:
        """
        Update the exchange rate for a given currency.
        
        :param currency: The currency to update.
        :param new_rate: The new exchange rate.
        :return: True if successfully updated, False if the currency does not exist.
        """
        if currency not in self.rates:
            return False
        self.rates[currency] = new_rate
        return True