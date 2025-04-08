class StockPortfolioTracker:
    """
    Tracks a stock portfolio, allowing to add, remove, buy, and sell stocks,
    calculate the total portfolio value, and get a summary of the portfolio.
    """

    def __init__(self, cash_balance):
        """
        Initializes the StockPortfolioTracker with a cash balance and an empty portfolio.

        Args:
            cash_balance (float): The initial cash balance.
        """
        self.portfolio = {}  # Use a dictionary to store stocks with stock name as key
        self.cash_balance = cash_balance

    def add_stock(self, stock):
        """
        Adds a stock to the portfolio.  If the stock already exists, its quantity is increased.

        Args:
            stock (dict): A dictionary containing stock information with keys "name", "price", and "quantity".
        """
        stock_name = stock["name"]
        stock_quantity = stock["quantity"]

        if stock_name in self.portfolio:
            self.portfolio[stock_name]["quantity"] += stock_quantity
        else:
            self.portfolio[stock_name] = {"price": stock["price"], "quantity": stock_quantity}

    def remove_stock(self, stock):
        """
        Removes a specified quantity of a stock from the portfolio.

        Args:
            stock (dict): A dictionary containing stock information with keys "name" and "quantity".

        Returns:
            bool: True if the stock was successfully removed, False otherwise (e.g., insufficient quantity).
        """
        stock_name = stock["name"]
        stock_quantity = stock["quantity"]

        if stock_name in self.portfolio:
            if self.portfolio[stock_name]["quantity"] >= stock_quantity:
                self.portfolio[stock_name]["quantity"] -= stock_quantity
                if self.portfolio[stock_name]["quantity"] == 0:
                    del self.portfolio[stock_name]
                return True
            else:
                return False
        else:
            return False

    def buy_stock(self, stock):
        """
        Buys a stock and adds it to the portfolio.

        Args:
            stock (dict): A dictionary containing stock information with keys "name", "price", and "quantity".

        Returns:
            bool: True if the stock was bought successfully, False if the cash balance is insufficient.
        """
        stock_name = stock["name"]
        stock_price = stock["price"]
        stock_quantity = stock["quantity"]
        cost = stock_price * stock_quantity

        if self.cash_balance >= cost:
            self.cash_balance -= cost
            # Create a copy of the stock dict to avoid modifying the original
            stock_copy = {"name": stock_name, "price": stock_price, "quantity": stock_quantity}
            self.add_stock(stock_copy)
            return True
        else:
            return False

    def sell_stock(self, stock):
        """
        Sells a stock from the portfolio, adding the proceeds to the cash balance.

        Args:
            stock (dict): A dictionary containing stock information with keys "name", "price", and "quantity".

        Returns:
            bool: True if the stock was sold successfully, False if the quantity of the stock is insufficient.
        """
        stock_name = stock["name"]
        stock_price = stock["price"]
        stock_quantity = stock["quantity"]

        if stock_name in self.portfolio:
            if self.portfolio[stock_name]["quantity"] >= stock_quantity:
                self.portfolio[stock_name]["quantity"] -= stock_quantity
                self.cash_balance += stock_price * stock_quantity
                if self.portfolio[stock_name]["quantity"] == 0:
                    del self.portfolio[stock_name]
                return True
            else:
                return False
        else:
            return False

    def calculate_portfolio_value(self):
        """
        Calculates the total value of the portfolio (cash balance + value of all stocks).

        Returns:
            float: The total value of the portfolio.
        """
        portfolio_value = self.cash_balance

        for stock_name, stock in self.portfolio.items():
            portfolio_value += stock["price"] * stock["quantity"]

        return portfolio_value

    def get_portfolio_summary(self):
        """
        Provides a summary of the portfolio, including the total value and a list of stock holdings.

        Returns:
            tuple: A tuple containing the total value of the portfolio (float) and a list of dictionaries,
                   where each dictionary represents a stock holding with keys "name" and "value".
        """
        total_value = self.calculate_portfolio_value()
        stock_values = []

        for stock_name, stock in self.portfolio.items():
            stock_values.append({"name": stock_name, "value": stock["price"] * stock["quantity"]})

        return total_value, stock_values

    def get_stock_value(self, stock):
        """
        Calculates the value of a given stock based on its price and quantity.

        Args:
            stock (dict): A dictionary containing stock information with keys "name", "price", and "quantity".

        Returns:
            float: The value of the stock.
        """
        return stock["price"] * stock["quantity"]