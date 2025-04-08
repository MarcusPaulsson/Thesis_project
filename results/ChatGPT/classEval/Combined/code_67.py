class Order:
    """
    The class manages restaurant orders by allowing the addition of dishes, calculation of the total cost, and checkout.
    """

    def __init__(self):
        """
        Initialize the order management system. 
        - self.menu stores the dishes of restaurant inventory.
        - self.selected_dishes stores the dishes selected by customer.
        - self.sales stores the sales multiplier for each dish.
        """
        self.menu = []
        self.selected_dishes = []
        self.sales = {}

    def add_dish(self, dish):
        """
        Add a dish to the selected dishes if the count is available in the menu.
        
        :param dish: dict, the information of dish. 
                     dish = {"dish": dish name, "count": count, "price": price}
        :return: True if successfully added, or False otherwise.
        """
        for menu_dish in self.menu:
            if menu_dish["dish"] == dish["dish"]:
                if menu_dish["count"] >= dish["count"]:
                    menu_dish["count"] -= dish["count"]
                    self.selected_dishes.append(dish)
                    return True
                return False
        return False

    def calculate_total(self):
        """
        Calculate the total price of dishes that have been ordered.
        
        :return: float, the final total price.
        """
        total = sum(selected["price"] * self.sales.get(selected["dish"], 1) * selected["count"]
                     for selected in self.selected_dishes)
        return total

    def checkout(self):
        """
        Check out the dishes ordered. If the selected dishes are not empty, calculate the total.
        
        :return: False if the selected dishes are empty, or total (return value of calculate_total) otherwise.
        """
        if not self.selected_dishes:
            return False
        total = self.calculate_total()
        self.selected_dishes.clear()  # Clear the selected dishes after checkout
        return total