class StockPortfolioTracker:
    """
    Tracks a stock portfolio, allowing to add, remove, buy, and sell stocks,
    calculate the total portfolio value, and obtain a summary.
    """

    def __init__(self, cash_balance):
        """
        Initializes the StockPortfolioTracker with a cash balance and an empty portfolio.

        :param cash_balance: The initial cash balance for the portfolio.
        :type cash_balance: float
        """
        self.portfolio = []
        self.cash_balance = cash_balance

    def add_stock(self, stock):
        """
        Adds a stock to the portfolio.  If the stock already exists, the quantity is increased.

        :param stock: A dictionary representing the stock, with keys "name", "price", and "quantity".
        :type stock: dict
        :raises TypeError: if stock is not a dictionary
        :raises KeyError: if stock does not contain the keys "name", "price", and "quantity"
        """
        if not isinstance(stock, dict):
            raise TypeError("Stock must be a dictionary.")
        if not all(key in stock for key in ("name", "price", "quantity")):
            raise KeyError("Stock must contain 'name', 'price', and 'quantity' keys.")

        stock_name = stock["name"]
        stock_quantity = stock["quantity"]

        for existing_stock in self.portfolio:
            if existing_stock["name"] == stock_name:
                existing_stock["quantity"] += stock_quantity
                return

        self.portfolio.append(stock)

    def remove_stock(self, stock):
        """
        Removes a stock from the portfolio. If the quantity to remove is greater than the quantity owned,
        the function returns False.  If the quantity to remove matches the quantity owned, the stock is removed.
        If the stock doesn't exist, the function returns False.

        :param stock: A dictionary representing the stock to remove, with keys "name" and "quantity".
        :type stock: dict
        :return: True if the stock was successfully removed, False otherwise.
        :rtype: bool
        :raises TypeError: if stock is not a dictionary
        :raises KeyError: if stock does not contain the keys "name" and "quantity"
        """
        if not isinstance(stock, dict):
            raise TypeError("Stock must be a dictionary.")
        if not all(key in stock for key in ("name", "quantity")):
            raise KeyError("Stock must contain 'name' and 'quantity' keys.")

        stock_name = stock["name"]
        stock_quantity = stock["quantity"]

        for existing_stock in self.portfolio:
            if existing_stock["name"] == stock_name:
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
        Buys a stock and adds it to the portfolio.  If sufficient cash is available, the stock is added,
        and the cash balance is reduced.

        :param stock: A dictionary representing the stock to buy, with keys "name", "price", and "quantity".
        :type stock: dict
        :return: True if the stock was bought successfully, False if the cash balance is insufficient.
        :rtype: bool
        :raises TypeError: if stock is not a dictionary
        :raises KeyError: if stock does not contain the keys "name", "price", and "quantity"
        """
        if not isinstance(stock, dict):
            raise TypeError("Stock must be a dictionary.")
        if not all(key in stock for key in ("name", "price", "quantity")):
            raise KeyError("Stock must contain 'name', 'price', and 'quantity' keys.")

        cost = stock["price"] * stock["quantity"]

        if self.cash_balance >= cost:
            self.cash_balance -= cost
            self.add_stock(stock)
            return True
        else:
            return False

    def sell_stock(self, stock):
        """
        Sells a stock from the portfolio and adds the proceeds to the cash balance.

        :param stock: A dictionary representing the stock to sell, with keys "name", "price", and "quantity".
        :type stock: dict
        :return: True if the stock was sold successfully, False if the quantity of the stock is insufficient.
        :rtype: bool
        :raises TypeError: if stock is not a dictionary
        :raises KeyError: if stock does not contain the keys "name", "price", and "quantity"
        """
        if not isinstance(stock, dict):
            raise TypeError("Stock must be a dictionary.")
        if not all(key in stock for key in ("name", "price", "quantity")):
            raise KeyError("Stock must contain 'name', 'price', and 'quantity' keys.")

        stock_name = stock["name"]
        stock_price = stock["price"]
        stock_quantity = stock["quantity"]

        for existing_stock in self.portfolio:
            if existing_stock["name"] == stock_name:
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
        Calculates the total value of the portfolio, including cash balance and stock holdings.

        :return: The total value of the portfolio.
        :rtype: float
        """
        total_value = self.cash_balance
        for stock in self.portfolio:
            total_value += stock["price"] * stock["quantity"]
        return total_value

    def get_portfolio_summary(self):
        """
        Gets a summary of the portfolio, including the total value and a list of stock holdings with their values.

        :return: A tuple containing the total value of the portfolio and a list of dictionaries,
                 where each dictionary represents a stock holding with its name and value.
        :rtype: tuple(float, list(dict))
        """
        total_value = self.calculate_portfolio_value()
        stock_values = []
        for stock in self.portfolio:
            stock_values.append({"name": stock["name"], "value": stock["price"] * stock["quantity"]})
        return total_value, stock_values

    def get_stock_value(self, stock):
        """
        Gets the value of a given stock based on its price and quantity.

        :param stock: A dictionary representing the stock, with keys "price" and "quantity".
        :type stock: dict
        :return: The value of the stock.
        :rtype: float
        :raises TypeError: if stock is not a dictionary
        :raises KeyError: if stock does not contain the keys "price" and "quantity"
        """
        if not isinstance(stock, dict):
            raise TypeError("Stock must be a dictionary.")
        if not all(key in stock for key in ("price", "quantity")):
            raise KeyError("Stock must contain 'price' and 'quantity' keys.")
        return stock["price"] * stock["quantity"]