class Order:
    """
    The class manages restaurant orders by allowing the addition of dishes, calculation of the total cost, and checkout.
    """

    def __init__(self):
        """
        Initialize the order management system.

        self.menu: Stores the restaurant's inventory of dishes.
            Format: [{"dish": dish_name, "price": price, "count": count}, ...]
        self.selected_dishes: Stores the dishes selected by the customer.
            Format: [{"dish": dish_name, "count": count, "price": price}, ...]
        self.sales: Stores the sales rate for each dish.
            Format: {dish_name: sales_rate}
        """
        self.menu = []
        self.selected_dishes = []
        self.sales = {}

    def add_dish(self, dish):
        """
        Adds a dish to the order if it's available in the menu and the requested count is valid.

        Args:
            dish (dict): A dictionary containing the dish's information.
                Format: {"dish": dish_name, "count": count, "price": price}

        Returns:
            bool: True if the dish was successfully added, False otherwise.
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
        Completes the order and calculates the final total.

        Returns:
            float: The total price of the order if successful, False if no dishes were selected.
        """
        if not self.selected_dishes:
            return False

        total = self.calculate_total()
        self.selected_dishes = []  # Clear selected dishes after checkout
        return total