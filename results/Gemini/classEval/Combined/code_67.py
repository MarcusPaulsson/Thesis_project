class Order:
    """
    The class manages restaurant orders by allowing the addition of dishes, calculation of the total cost, and checkout.
    """

    def __init__(self):
        """
        Initialize the order management system.

        self.menu stores the dishes of restaurant inventory.
        Format: [{"dish": dish name, "price": price, "count": count}, ...]

        self.selected_dishes stores the dishes selected by customer.
        Format: [{"dish": dish name, "count": count, "price": price}, ...]

        self.sales stores the sales rate of each dish.
        Format: {dish name: sales_rate}
        """
        self.menu = []
        self.selected_dishes = []
        self.sales = {}

    def add_dish(self, dish):
        """
        Adds a dish to the order if it's available in the menu and the requested count is valid.

        :param dish: dict, the information of the dish to add.
                     Format: {"dish": dish name, "count": count, "price": price}
        :return: True if the dish was successfully added, False otherwise.
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

        return False  # Dish not found in menu

    def calculate_total(self):
        """
        Calculates the total price of the dishes in the order, considering sales rates.

        :return: float, the total price of the order.
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
        Completes the order, calculates the total, updates the menu, and clears the selected dishes.

        :return: float, the total price of the order if successful, False if no dishes were selected.
        """
        if not self.selected_dishes:
            return False

        total = self.calculate_total()

        # Update menu counts after checkout (more robust approach)
        for selected_dish in self.selected_dishes:
            dish_name = selected_dish["dish"]
            dish_count = selected_dish["count"]
            for menu_dish in self.menu:
                if menu_dish["dish"] == dish_name:
                    break # No need to update here, already updated in add_dish

        self.selected_dishes = []  # Clear selected dishes after checkout
        return total