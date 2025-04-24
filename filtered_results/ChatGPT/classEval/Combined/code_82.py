class StockPortfolioTracker:
    """
    A class to track a stock portfolio, allowing for adding, removing, buying, and selling stocks,
    as well as calculating the total portfolio value and obtaining a summary.
    """

    def __init__(self, cash_balance):
        """
        Initialize the StockPortfolioTracker with a cash balance and an empty portfolio.
        :param cash_balance: Initial cash balance for the portfolio.
        """
        self.portfolio = []
        self.cash_balance = cash_balance

    def add_stock(self, stock):
        """
        Add a stock to the portfolio or update the quantity if it already exists.
        :param stock: A dictionary with keys "name", "price", and "quantity".
        """
        for existing_stock in self.portfolio:
            if existing_stock['name'] == stock['name']:
                existing_stock['quantity'] += stock['quantity']
                return
        self.portfolio.append(stock)

    def remove_stock(self, stock):
        """
        Remove a specified quantity of a stock from the portfolio.
        :param stock: A dictionary with keys "name", "price", and "quantity".
        :return: True if the stock was removed successfully, False otherwise.
        """
        for existing_stock in self.portfolio:
            if existing_stock['name'] == stock['name']:
                if existing_stock['quantity'] >= stock['quantity']:
                    existing_stock['quantity'] -= stock['quantity']
                    if existing_stock['quantity'] == 0:
                        self.portfolio.remove(existing_stock)
                    return True
                break
        return False

    def buy_stock(self, stock):
        """
        Buy a stock and add it to the portfolio if sufficient cash is available.
        :param stock: A dictionary with keys "name", "price", and "quantity".
        :return: True if the stock was bought successfully, False if insufficient funds.
        """
        total_cost = stock['price'] * stock['quantity']
        if total_cost > self.cash_balance:
            return False
        self.cash_balance -= total_cost
        self.add_stock(stock)
        return True

    def sell_stock(self, stock):
        """
        Sell a specified quantity of a stock and add the cash to the cash balance.
        :param stock: A dictionary with keys "name", "price", and "quantity".
        :return: True if the stock was sold successfully, False if insufficient quantity.
        """
        for existing_stock in self.portfolio:
            if existing_stock['name'] == stock['name']:
                if existing_stock['quantity'] >= stock['quantity']:
                    total_sale = stock['price'] * stock['quantity']
                    self.cash_balance += total_sale
                    existing_stock['quantity'] -= stock['quantity']
                    if existing_stock['quantity'] == 0:
                        self.portfolio.remove(existing_stock)
                    return True
                break
        return False

    def calculate_portfolio_value(self):
        """
        Calculate the total value of the portfolio, including cash and stock values.
        :return: The total value of the portfolio as a float.
        """
        total_value = self.cash_balance
        for stock in self.portfolio:
            total_value += stock['price'] * stock['quantity']
        return total_value

    def get_portfolio_summary(self):
        """
        Get a summary of the portfolio, including total value and individual stock values.
        :return: A tuple of the total value of the portfolio and a list of stock values.
        """
        total_value = self.calculate_portfolio_value()
        summary = [{'name': stock['name'], 'value': stock['price'] * stock['quantity']} for stock in self.portfolio]
        return total_value, summary

    def get_stock_value(self, stock):
        """
        Get the value of a specific stock based on its price and quantity.
        :param stock: A dictionary with keys "name", "price", and "quantity".
        :return: The value of the stock as a float.
        """
        return stock['price'] * stock['quantity']