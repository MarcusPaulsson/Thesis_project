class StockPortfolioTracker:
    """
    This is a class as StockPortfolioTracker that allows to add stocks, remove stocks, buy stocks, sell stocks, calculate the total value of the portfolio, and obtain a summary of the portfolio.
    """

    def __init__(self, cash_balance):
        """
        Initialize the StockPortfolioTracker class with a cash balance and an empty portfolio.
        """
        self.portfolio = {}  # Use a dictionary to store stocks, with stock name as key
        self.cash_balance = cash_balance

    def add_stock(self, stock_name, price, quantity):
        """
        Add a stock to the portfolio.
        :param stock_name: The name of the stock (string).
        :param price: The price of the stock (float).
        :param quantity: The quantity of the stock (int).
        """
        if stock_name in self.portfolio:
            self.portfolio[stock_name]['quantity'] += quantity
        else:
            self.portfolio[stock_name] = {'price': price, 'quantity': quantity}

    def remove_stock(self, stock_name, quantity_to_remove):
        """
        Remove a stock from the portfolio.
        :param stock_name: The name of the stock to remove (string).
        :param quantity_to_remove: The quantity of the stock to remove (int).
        :return: True if the stock was successfully removed, False otherwise.
        """
        if stock_name not in self.portfolio:
            return False

        if self.portfolio[stock_name]['quantity'] < quantity_to_remove:
            return False

        self.portfolio[stock_name]['quantity'] -= quantity_to_remove
        if self.portfolio[stock_name]['quantity'] == 0:
            del self.portfolio[stock_name]
        return True

    def buy_stock(self, stock_name, price, quantity):
        """
        Buy a stock and add it to the portfolio.
        :param stock_name: The name of the stock to buy (string).
        :param price: The price of the stock (float).
        :param quantity: The quantity of the stock to buy (int).
        :return: True if the stock was bought successfully, False if the cash balance is not enough.
        """
        cost = price * quantity
        if self.cash_balance >= cost:
            self.add_stock(stock_name, price, quantity)
            self.cash_balance -= cost
            return True
        else:
            return False

    def sell_stock(self, stock_name, price, quantity):
        """
        Sell a stock and remove it from the portfolio and add the cash to the cash balance.
        :param stock_name: The name of the stock to sell (string).
        :param price: The price of the stock (float).
        :param quantity: The quantity of the stock to sell (int).
        :return: True if the stock was sold successfully, False if the quantity of the stock is not enough.
        """
        if stock_name not in self.portfolio:
            return False

        if self.portfolio[stock_name]['quantity'] < quantity:
            return False

        self.remove_stock(stock_name, quantity)  # Remove using the remove_stock method
        self.cash_balance += price * quantity
        return True

    def calculate_portfolio_value(self):
        """
        Calculate the total value of the portfolio.
        :return: the total value of the portfolio, float.
        """
        total_value = self.cash_balance
        for stock_name, stock_data in self.portfolio.items():
            total_value += stock_data['price'] * stock_data['quantity']
        return total_value

    def get_portfolio_summary(self):
        """
        Get a summary of the portfolio.
        :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value"
        """
        total_value = self.calculate_portfolio_value()
        stock_values = []
        for stock_name, stock_data in self.portfolio.items():
            stock_values.append({"name": stock_name, "value": stock_data['price'] * stock_data['quantity']})
        return total_value, stock_values

    def get_stock_value(self, stock_name):
        """
        Get the value of a stock.
        :param stock_name: The name of the stock (string).
        :return: the value of the stock, float, or None if the stock is not in the portfolio.
        """
        if stock_name not in self.portfolio:
            return None
        stock_data = self.portfolio[stock_name]
        return stock_data['price'] * stock_data['quantity']