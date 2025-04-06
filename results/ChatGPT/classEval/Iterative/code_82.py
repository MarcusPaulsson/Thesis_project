class StockPortfolioTracker:
    """
    A class to track a stock portfolio, allowing for adding, removing, buying, and selling stocks, 
    calculating the total value of the portfolio, and obtaining a summary of the portfolio.
    """

    def __init__(self, cash_balance):
        """
        Initialize the StockPortfolioTracker class with a cash balance and an empty portfolio.
        :param cash_balance: Initial cash balance, float.
        """
        self.portfolio = []
        self.cash_balance = cash_balance

    def add_stock(self, stock):
        """
        Add a stock to the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity".
        """
        if self.validate_stock(stock):
            self.portfolio.append(stock)

    def remove_stock(self, stock):
        """
        Remove a stock from the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity".
        :return: True if the stock was removed, False otherwise.
        """
        for s in self.portfolio:
            if s['name'] == stock['name'] and s['price'] == stock['price'] and s['quantity'] == stock['quantity']:
                self.portfolio.remove(s)
                return True
        return False

    def buy_stock(self, stock):
        """
        Buy a stock and add it to the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity".
        :return: True if the stock was bought successfully, False if the cash balance is not enough.
        """
        total_cost = stock['price'] * stock['quantity']
        if total_cost <= self.cash_balance and self.validate_stock(stock):
            self.cash_balance -= total_cost
            self.add_stock(stock)
            return True
        return False

    def sell_stock(self, stock):
        """
        Sell a stock and remove it from the portfolio, adding the cash to the cash balance.
        :param stock: a dictionary with keys "name", "price", and "quantity".
        :return: True if the stock was sold successfully, False if the quantity of the stock is not enough.
        """
        for s in self.portfolio:
            if s['name'] == stock['name'] and s['quantity'] >= stock['quantity']:
                total_sale = s['price'] * stock['quantity']
                self.cash_balance += total_sale
                s['quantity'] -= stock['quantity']
                if s['quantity'] == 0:
                    self.remove_stock(s)
                return True
        return False

    def calculate_portfolio_value(self):
        """
        Calculate the total value of the portfolio.
        :return: the total value of the portfolio, float.
        """
        return sum(s['price'] * s['quantity'] for s in self.portfolio)

    def get_portfolio_summary(self):
        """
        Get a summary of the portfolio.
        :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value".
        """
        total_value = self.calculate_portfolio_value()
        summary = [{'name': s['name'], 'value': s['price'] * s['quantity']} for s in self.portfolio]
        return total_value, summary

    def get_stock_value(self, stock):
        """
        Get the value of a stock.
        :param stock: a dictionary with keys "name", "price", and "quantity".
        :return: the value of the stock, float.
        """
        return stock['price'] * stock['quantity']

    def validate_stock(self, stock):
        """
        Validate stock dictionary format.
        :param stock: a dictionary with keys "name", "price", and "quantity".
        :return: True if valid, False otherwise.
        """
        return all(key in stock for key in ["name", "price", "quantity"]) and isinstance(stock['quantity'], int) and stock['quantity'] > 0