class Order:
    """
    The class manages restaurant orders by allowing the addition of dishes, calculation of the total cost, and checkout.
    """

    def __init__(self):
        """
        Initialize the order management system.
        self.menu stores the dishes of restaurant inventory.
        self.selected_dishes stores the dishes selected by the customer.
        self.sales stores the sales of each dish.
        """
        self.menu = []
        self.selected_dishes = []
        self.sales = {}

    def add_dish(self, dish):
        """
        Check the self.menu and add into self.selected_dishes if the dish count is valid.
        If the dish has successfully been added, change the count in self.menu.
        :param dish: dict, the information of dish. dish = {"dish": dish name, "count": count, price: price}
        :return: True if successfully added, or False otherwise.
        """
        for menu_dish in self.menu:
            if menu_dish['dish'] == dish['dish']:
                if menu_dish['count'] >= dish['count']:
                    menu_dish['count'] -= dish['count']
                    self.selected_dishes.append({"dish": dish['dish'], "count": dish['count'], "price": dish['price']})
                    return True
                else:
                    return False
        return False

    def calculate_total(self):
        """
        Calculate the total price of dishes that have been ordered. 
        Multiply the count, price, and sales.
        :return: float, the final total price.
        """
        total = 0
        for selected in self.selected_dishes:
            dish_name = selected['dish']
            price = selected['price']
            count = selected['count']
            total += price * count * self.sales.get(dish_name, 1)
        return total

    def checkout(self):
        """
        Check out the dishes ordered. If the self.selected_dishes is not empty, invoke the calculate_total
        method to check out.
        :return: False if the self.selected_dishes is empty, or total (return value of calculate_total) otherwise.
        """
        if not self.selected_dishes:
            return False
        total = self.calculate_total()
        self.selected_dishes.clear()  # Clear selected dishes after checkout
        return total