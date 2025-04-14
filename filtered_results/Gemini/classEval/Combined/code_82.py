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
        """
        stock_name = stock["name"]
        stock_price = stock["price"]
        stock_quantity = stock["quantity"]

        for existing_stock in self.portfolio:
            if existing_stock["name"] == stock_name and existing_stock["price"] == stock_price:
                existing_stock["quantity"] += stock_quantity
                return

        self.portfolio.append(stock)

    def remove_stock(self, stock):
        """
        Remove a stock from the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        """
        stock_name = stock["name"]
        stock_price = stock["price"]
        stock_quantity = stock["quantity"]

        for existing_stock in self.portfolio:
            if existing_stock["name"] == stock_name and existing_stock["price"] == stock_price:
                if existing_stock["quantity"] >= stock_quantity:
                    existing_stock["quantity"] -= stock_quantity
                    if existing_stock["quantity"] == 0:
                        self.portfolio.remove(existing_stock)
                    return True
                else:
                    return False
        return False

    def buy_stock(self, stock):
        """
        Buy a stock and add it to the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: True if the stock was bought successfully, False if the cash balance is not enough.
        """
        stock_name = stock["name"]
        stock_price = stock["price"]
        stock_quantity = stock["quantity"]

        cost = stock_price * stock_quantity

        if self.cash_balance >= cost:
            self.cash_balance -= cost
            self.add_stock(stock)
            return True
        else:
            return False

    def sell_stock(self, stock):
        """
        Sell a stock and remove it from the portfolio and add the cash to the cash balance.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: True if the stock was sold successfully, False if the quantity of the stock is not enough.
        """
        stock_name = stock["name"]
        stock_price = stock["price"]
        stock_quantity = stock["quantity"]

        for existing_stock in self.portfolio:
            if existing_stock["name"] == stock_name and existing_stock["price"] == stock_price:
                if existing_stock["quantity"] >= stock_quantity:
                    self.cash_balance += stock_price * stock_quantity
                    existing_stock["quantity"] -= stock_quantity
                    if existing_stock["quantity"] == 0:
                        self.portfolio.remove(existing_stock)
                    return True
                else:
                    return False
        return False

    def calculate_portfolio_value(self):
        """
        Calculate the total value of the portfolio.
        :return: the total value of the portfolio, float.
        """
        total_value = self.cash_balance
        for stock in self.portfolio:
            total_value += stock["price"] * stock["quantity"]
        return total_value

    def get_portfolio_summary(self):
        """
        Get a summary of the portfolio.
        :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value"
        """
        total_value = self.calculate_portfolio_value()
        stock_values = []
        for stock in self.portfolio:
            stock_values.append({"name": stock["name"], "value": stock["price"] * stock["quantity"]})
        return total_value, stock_values

    def get_stock_value(self, stock):
        """
        Get the value of a stock.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: the value of the stock, float.
        """
        return stock["price"] * stock["quantity"]