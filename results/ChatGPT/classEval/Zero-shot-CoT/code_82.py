class StockPortfolioTracker:
    """
    This is a class as StockPortfolioTracker that allows to add stocks, remove stocks, buy stocks, sell stocks, calculate the total value of the portfolio, and obtain a summary of the portfolio.
    """

    def __init__(self, cash_balance):
        """
        Initialize the StockPortfolioTracker class with a cash balance and an empty portfolio.
        """
        self.portfolio = []
        self.cash_balance = cash_balance

    def add_stock(self, stock):
        """
        Add a stock to the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.add_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        >>> tracker.portfolio
        [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        """
        self.portfolio.append(stock)

    def remove_stock(self, stock):
        """
        Remove a stock from the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.remove_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        True
        >>> tracker.portfolio
        []
        """
        for s in self.portfolio:
            if s['name'] == stock['name'] and s['price'] == stock['price'] and s['quantity'] == stock['quantity']:
                self.portfolio.remove(s)
                return True
        return False

    def buy_stock(self, stock):
        """
        Buy a stock and add it to the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: True if the stock was bought successfully, False if the cash balance is not enough.
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.buy_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        True
        >>> tracker.portfolio
        [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        """
        total_cost = stock['price'] * stock['quantity']
        if total_cost > self.cash_balance:
            return False
        self.cash_balance -= total_cost
        self.add_stock(stock)
        return True

    def sell_stock(self, stock):
        """
        Sell a stock and remove it from the portfolio and add the cash to the cash balance.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: True if the stock was sold successfully, False if the quantity of the stock is not enough.
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.sell_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        True
        >>> tracker.portfolio
        []
        """
        for s in self.portfolio:
            if s['name'] == stock['name'] and s['price'] == stock['price'] and s['quantity'] == stock['quantity']:
                self.cash_balance += s['price'] * s['quantity']
                self.remove_stock(s)
                return True
        return False

    def calculate_portfolio_value(self):
        """
        Calculate the total value of the portfolio.
        :return: the total value of the portfolio, float.
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.calculate_portfolio_value()
        1500.0
        """
        total_value = sum(s['price'] * s['quantity'] for s in self.portfolio)
        return total_value

    def get_portfolio_summary(self):
        """
        Get a summary of the portfolio.
        :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value"
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.get_portfolio_summary()
        (1500.0, [{'name': 'AAPL', 'value': 1500.0}])
        """
        total_value = self.calculate_portfolio_value()
        summary = [{'name': s['name'], 'value': s['price'] * s['quantity']} for s in self.portfolio]
        return (total_value, summary)

    def get_stock_value(self, stock):
        """
        Get the value of a stock.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: the value of the stock, float.
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.get_stock_value({"name": "AAPL", "price": 150.0, "quantity": 10})
        1500.0
        """
        return stock['price'] * stock['quantity']