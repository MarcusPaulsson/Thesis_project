class Order:
    """
    The class manages restaurant orders by allowing the addition of dishes, calculation of the total cost, and checkout.
    """

    def __init__(self):
        """
        Initialize the order management system
        self.menu stores the dishes of restaurant inventory
        menu = [{"dish": dish name, "price": price, "count": count}, ...]
        self.selected_dishes stores the dishes selected by customer
        selected_dish = {"dish": dish name, "count": count, price: price}
        self.sales stores the sales of each dish
        sales = {dish name: sales}
        """
        self.menu = []
        self.selected_dishes = []
        self.sales = {}

    def add_dish(self, dish):
        """
        Check the self.menu and add into self.selected_dishes if the dish count is valid.
        And if the dish has successfully been added, change the count in self.menu.
        :param dish: dict, the information of dish. dish = {"dish": dish name, "count": count, price: price}
        :return: True if successfully added, or False otherwise.
        """
        dish_name = dish["dish"]
        count = dish["count"]
        
        # Find the dish in the menu
        for menu_dish in self.menu:
            if menu_dish["dish"] == dish_name:
                if count <= menu_dish["count"]:
                    # Add to selected_dishes
                    self.selected_dishes.append({"dish": dish_name, "count": count, "price": menu_dish["price"]})
                    # Update the menu count
                    menu_dish["count"] -= count
                    return True
                else:
                    return False
        return False

    def calculate_total(self):
        """
        Calculate the total price of dishes that have been ordered. Multiply the count, price and sales.
        :return total: float, the final total price.
        """
        total = 0.0
        for selected in self.selected_dishes:
            dish_name = selected["dish"]
            if dish_name in self.sales:
                total += selected["count"] * selected["price"] * self.sales[dish_name]
        return total

    def checkout(self):
        """
        Check out the dishes ordered. If the self.selected_dishes is not empty, invoke the calculate_total
        method to check out.
        :return False if the self.selected_dishes is empty, or total (return value of calculate_total) otherwise.
        """
        if not self.selected_dishes:
            return False
        total = self.calculate_total()
        # Clear selected dishes after checkout
        self.selected_dishes = []
        return total