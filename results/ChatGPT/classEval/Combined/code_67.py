class Order:
    """
    Manages restaurant orders by allowing the addition of dishes, calculation of the total cost, and checkout.
    """

    def __init__(self):
        """
        Initialize the order management system.
        """
        self.menu = []  # List of available dishes
        self.selected_dishes = []  # Dishes selected by the customer
        self.sales = {}  # Discounts for each dish

    def add_dish(self, dish):
        """
        Adds a dish to the selected dishes if the count is valid and updates the menu accordingly.
        
        :param dish: dict, information of the dish. 
                     dish = {"dish": dish name, "count": count, "price": price}
        :return: True if successfully added, False otherwise.
        """
        for menu_dish in self.menu:
            if menu_dish["dish"] == dish["dish"]:
                if dish["count"] > menu_dish["count"]:
                    return False  # Not enough dishes available
                # Update menu and selected dishes
                menu_dish["count"] -= dish["count"]
                self.selected_dishes.append({"dish": dish["dish"], "count": dish["count"], "price": dish["price"]})
                return True
        return False

    def calculate_total(self):
        """
        Calculates the total price of the selected dishes, considering discounts.
        
        :return: float, the final total price.
        """
        total = 0.0
        for selected in self.selected_dishes:
            sales_multiplier = self.sales.get(selected["dish"], 1)
            total += selected["count"] * selected["price"] * sales_multiplier
        return total

    def checkout(self):
        """
        Finalizes the order and clears selected dishes.
        
        :return: total if dishes were ordered, False if no dishes were selected.
        """
        if not self.selected_dishes:
            return False
        total = self.calculate_total()
        self.selected_dishes.clear()  # Clear selected dishes after checkout
        return total