class StockPortfolioTracker:
    """
    A class to track a stock portfolio, allowing for adding, removing, buying, and selling stocks,
    as well as calculating the total portfolio value and generating a summary of the portfolio.
    """

    def __init__(self, cash_balance):
        """
        Initialize the StockPortfolioTracker with a cash balance and an empty portfolio.
        :param cash_balance: Initial cash balance, float.
        """
        self.portfolio = []
        self.cash_balance = cash_balance

    def add_stock(self, stock):
        """
        Add a stock to the portfolio, or increase the quantity if it already exists.
        :param stock: A dictionary containing 'name', 'price', and 'quantity'.
        """
        for item in self.portfolio:
            if item['name'] == stock['name']:
                item['quantity'] += stock['quantity']
                return
        self.portfolio.append(stock)

    def remove_stock(self, stock):
        """
        Remove a stock from the portfolio if it matches the name and quantity.
        :param stock: A dictionary containing 'name', 'price', and 'quantity'.
        :return: True if the stock was removed, False otherwise.
        """
        for item in self.portfolio:
            if item['name'] == stock['name'] and item['quantity'] == stock['quantity']:
                self.portfolio.remove(item)
                return True
        return False

    def buy_stock(self, stock):
        """
        Buy a stock and add it to the portfolio.
        :param stock: A dictionary containing 'name', 'price', and 'quantity'.
        :return: True if the stock was bought successfully, False if insufficient cash.
        """
        total_cost = stock['price'] * stock['quantity']
        if total_cost > self.cash_balance:
            return False
        self.cash_balance -= total_cost
        self.add_stock(stock)
        return True

    def sell_stock(self, stock):
        """
        Sell a stock from the portfolio and update cash balance.
        :param stock: A dictionary containing 'name', 'price', and 'quantity'.
        :return: True if the stock was sold successfully, False if insufficient quantity.
        """
        for item in self.portfolio:
            if item['name'] == stock['name']:
                if item['quantity'] >= stock['quantity']:
                    total_sale = stock['price'] * stock['quantity']
                    self.cash_balance += total_sale
                    item['quantity'] -= stock['quantity']
                    if item['quantity'] == 0:
                        self.portfolio.remove(item)
                    return True
        return False

    def calculate_portfolio_value(self):
        """
        Calculate the total value of the portfolio including cash balance.
        :return: Total portfolio value, float.
        """
        total_value = self.cash_balance
        for item in self.portfolio:
            total_value += item['price'] * item['quantity']
        return total_value

    def get_portfolio_summary(self):
        """
        Get a summary of the portfolio including total value and individual stock values.
        :return: A tuple of total value and a list of stock summary dictionaries.
        """
        total_value = self.calculate_portfolio_value()
        summary = [{'name': item['name'], 'value': item['price'] * item['quantity']} for item in self.portfolio]
        return total_value, summary

    def get_stock_value(self, stock):
        """
        Calculate the value of a specific stock.
        :param stock: A dictionary containing 'name', 'price', and 'quantity'.
        :return: Value of the stock, float.
        """
        return stock['price'] * stock['quantity']