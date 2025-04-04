class Order:
    """
    The class manages restaurant orders by allowing the addition of dishes, calculation of the total cost, and checkout.
    """

    def __init__(self):
        """
        Initialize the order management system.
        self.menu stores the dishes of restaurant inventory.
        menu = [{"dish": dish_name, "price": price, "count": count}, ...]
        self.selected_dishes stores the dishes selected by customers.
        selected_dishes = [{"dish": dish_name, "count": count, "price": price}, ...]
        self.sales stores the sales of each dish.
        sales = {dish_name: sales}
        """
        self.menu = []
        self.selected_dishes = []
        self.sales = {}

    def add_dish(self, dish):
        """
        Check the self.menu and add to self.selected_dishes if the dish count is valid.
        If the dish has been successfully added, change the count in self.menu.
        :param dish: dict, the information of dish. dish = {"dish": dish_name, "count": count, price: price}
        :return: True if successfully added, or False otherwise.
        """
        for menu_item in self.menu:
            if menu_item['dish'] == dish['dish']:
                if menu_item['count'] >= dish['count']:
                    self.selected_dishes.append(dish)
                    menu_item['count'] -= dish['count']
                    return True
                break
        return False

    def calculate_total(self):
        """
        Calculate the total price of dishes that have been ordered. Multiply the count, price, and sales.
        :return total: float, the final total price.
        """
        total = 0.0
        for selected in self.selected_dishes:
            dish_name = selected['dish']
            price = selected['price']
            count = selected['count']
            discount = self.sales.get(dish_name, 1)  # Default discount is 1 (no discount)
            total += price * count * discount
        return total

    def checkout(self):
        """
        Check out the dishes ordered. If self.selected_dishes is not empty, invoke the calculate_total method.
        :return: False if self.selected_dishes is empty, or total (return value of calculate_total) otherwise.
        """
        if not self.selected_dishes:
            return False
        return self.calculate_total()