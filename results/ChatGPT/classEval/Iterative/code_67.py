class Order:
    """
    The class manages restaurant orders by allowing the addition of dishes, calculation of the total cost, and checkout.
    """

    def __init__(self):
        """
        Initialize the order management system.
        self.menu stores the dishes of restaurant inventory.
        menu = [{"dish": dish name, "price": price, "count": count}, ...]
        self.selected_dishes stores the dishes selected by customer.
        selected_dish = {"dish": dish name, "count": count, price: price}
        self.sales stores the sales of each dish.
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
        for menu_item in self.menu:
            if menu_item["dish"] == dish["dish"]:
                if menu_item["count"] >= dish["count"]:
                    menu_item["count"] -= dish["count"]
                    selected_dish = {"dish": dish["dish"], "count": dish["count"], "price": dish["price"]}
                    self.selected_dishes.append(selected_dish)
                    return True
                else:
                    return False
        return False

    def calculate_total(self):
        """
        Calculate the total price of dishes that have been ordered. Multiply the count, price and sales.
        :return total: float, the final total price.
        """
        total = 0
        for selected in self.selected_dishes:
            dish_name = selected["dish"]
            price_multiplier = self.sales.get(dish_name, 1)
            total += selected["count"] * selected["price"] * price_multiplier
        return total

    def checkout(self):
        """
        Check out the dishes ordered. If the self.selected_dishes is not empty,
        invoke the calculate_total method to check out.
        :return: False if the self.selected_dishes is empty, or total (return value of calculate_total) otherwise.
        """
        if not self.selected_dishes:
            return False
        return self.calculate_total()