class StockPortfolioTracker:
    """
    A class to track a stock portfolio, allowing addition, removal, buying, selling of stocks,
    and calculation of portfolio value and summaries.
    """

    def __init__(self, cash_balance):
        """
        Initialize the StockPortfolioTracker with a cash balance and an empty portfolio.
        :param cash_balance: Initial cash balance for transactions.
        """
        self.portfolio = []
        self.cash_balance = cash_balance

    def add_stock(self, stock):
        """
        Add a stock to the portfolio or update the quantity if it already exists.
        :param stock: A dictionary with keys "name", "price", and "quantity".
        """
        for item in self.portfolio:
            if item["name"] == stock["name"]:
                item["quantity"] += stock["quantity"]
                return
        self.portfolio.append(stock)

    def remove_stock(self, stock):
        """
        Remove a stock from the portfolio if the quantity matches.
        :param stock: A dictionary with keys "name", "price", and "quantity".
        :return: True if the stock was removed successfully, False otherwise.
        """
        for item in self.portfolio:
            if item["name"] == stock["name"] and item["quantity"] == stock["quantity"]:
                self.portfolio.remove(item)
                return True
        return False

    def buy_stock(self, stock):
        """
        Buy a stock and add it to the portfolio.
        :param stock: A dictionary with keys "name", "price", and "quantity".
        :return: True if the stock was bought successfully, False if insufficient funds.
        """
        total_cost = stock["price"] * stock["quantity"]
        if total_cost <= self.cash_balance:
            self.cash_balance -= total_cost
            self.add_stock(stock)
            return True
        return False

    def sell_stock(self, stock):
        """
        Sell a stock and update the portfolio and cash balance.
        :param stock: A dictionary with keys "name", "price", and "quantity".
        :return: True if the stock was sold successfully, False if insufficient quantity.
        """
        for item in self.portfolio:
            if item["name"] == stock["name"]:
                if item["quantity"] >= stock["quantity"]:
                    item["quantity"] -= stock["quantity"]
                    self.cash_balance += stock["price"] * stock["quantity"]
                    if item["quantity"] == 0:
                        self.portfolio.remove(item)
                    return True
        return False

    def calculate_portfolio_value(self):
        """
        Calculate the total value of the portfolio.
        :return: Total value of the portfolio as a float.
        """
        total_value = self.cash_balance
        for item in self.portfolio:
            total_value += item["price"] * item["quantity"]
        return total_value

    def get_portfolio_summary(self):
        """
        Get a summary of the portfolio.
        :return: A tuple containing total portfolio value and a list of stock values.
        """
        total_value = self.calculate_portfolio_value()
        stock_summary = [{"name": item["name"], "value": item["price"] * item["quantity"]} for item in self.portfolio]
        return total_value, stock_summary

    def get_stock_value(self, stock):
        """
        Calculate the value of a stock.
        :param stock: A dictionary with keys "name", "price", and "quantity".
        :return: The value of the stock as a float.
        """
        return stock["price"] * stock["quantity"]