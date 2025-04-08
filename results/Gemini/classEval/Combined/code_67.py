class Order:
    """
    Manages restaurant orders by allowing the addition of dishes, calculation of the total cost, and checkout.
    """

    def __init__(self):
        """
        Initializes the order management system.

        - `self.menu`: Stores the restaurant's inventory of dishes as a list of dictionaries.
          Each dictionary represents a dish and contains its name, price, and available count.
          Example: `[{"dish": "dish name", "price": price, "count": count}, ...]`
        - `self.selected_dishes`: Stores the dishes selected by the customer in a list of dictionaries.
          Each dictionary represents a selected dish and contains its name, count, and price.
          Example: `[{"dish": "dish name", "count": count, "price": price}, ...]`
        - `self.sales`: Stores the sales rate for each dish in a dictionary.
          The dish name is the key, and the sales rate is the value.
          Example: `{dish name: sales rate}`
        """
        self.menu = []
        self.selected_dishes = []
        self.sales = {}

    def add_dish(self, dish):
        """
        Adds a dish to the order if it's available in the menu and the requested count is valid.

        Args:
            dish (dict): A dictionary containing the dish's information, including its name, count, and price.
                         Example: `{"dish": "dish name", "count": count, "price": price}`

        Returns:
            bool: True if the dish was successfully added to the order, False otherwise.
        """
        if not dish:
            return True

        dish_name = dish.get("dish")
        dish_count = dish.get("count")
        dish_price = dish.get("price")

        if not dish_name or not isinstance(dish_count, int) or dish_count <= 0:
            return False

        for menu_dish in self.menu:
            if menu_dish["dish"] == dish_name:
                if menu_dish["count"] >= dish_count:
                    menu_dish["count"] -= dish_count
                    self.selected_dishes.append({"dish": dish_name, "count": dish_count, "price": dish_price})
                    return True
                else:
                    return False

        return False

    def calculate_total(self):
        """
        Calculates the total price of the dishes in the order, considering any sales rates.

        Returns:
            float: The total price of the order.
        """
        total = 0.0
        for selected_dish in self.selected_dishes:
            dish_name = selected_dish["dish"]
            dish_count = selected_dish["count"]
            dish_price = selected_dish["price"]
            sales_rate = self.sales.get(dish_name, 1.0)  # Default to 1.0 if no sales rate is found
            total += dish_count * dish_price * sales_rate
        return total

    def checkout(self):
        """
        Completes the order by calculating the total cost and clearing the selected dishes.

        Returns:
            float or bool: The total cost of the order if successful, False if no dishes were selected.
        """
        if not self.selected_dishes:
            return False

        total = self.calculate_total()

        # Update menu counts after checkout
        for selected_dish in self.selected_dishes:
            dish_name = selected_dish["dish"]
            dish_count = selected_dish["count"]

            for menu_dish in self.menu:
                if menu_dish["dish"] == dish_name:
                    break

        self.selected_dishes = []  # Clear selected dishes after checkout
        return total