class Order:
    """
    The class manages restaurant orders by allowing the addition of dishes, calculation of the total cost, and checkout.
    """

    def __init__(self):
        """
        Initialize the order management system.
        self.menu stores the dishes of restaurant inventory.
        menu = [{"dish": dish name, "price": price, "count": count}, ...]
        self.selected_dishes stores the dishes selected by the customer.
        selected_dish = {"dish": dish name, "count": count, "price": price}
        self.sales stores the sales of each dish.
        sales = {dish name: sales}
        """
        self.menu = []
        self.selected_dishes = []
        self.sales = {}

    def add_dish(self, dish):
        """
        Check the self.menu and add into self.selected_dish if the dish count is valid.
        And if the dish has successfully been added, change the count in self.menu.
        :param dish: dict, the information of dish. dish = {"dish": dish name, "count": count, "price": price}
        :return: True if successfully added, or False otherwise.
        """
        dish_name = dish.get("dish")
        dish_count = dish.get("count")
        dish_price = dish.get("price")

        if not dish_name or not dish_count or not dish_price:
            return False

        for menu_dish in self.menu:
            if menu_dish["dish"] == dish_name:
                if menu_dish["count"] >= dish_count:
                    self.selected_dishes.append({"dish": dish_name, "count": dish_count, "price": dish_price})
                    menu_dish["count"] -= dish_count
                    return True
                else:
                    return False
        return False

    def calculate_total(self):
        """
        Calculate the total price of dishes that have been ordered. Multiply the count, price, and sales.
        :return: float, the final total price.
        """
        total = 0.0
        for dish in self.selected_dishes:
            dish_name = dish["dish"]
            dish_count = dish["count"]
            dish_price = dish["price"]
            sales = self.sales.get(dish_name, 1.0)  # Default to 1.0 if no sales info
            total += dish_count * dish_price * sales
        return total

    def checkout(self):
        """
        Check out the dishes ordered.
        :return: False if self.selected_dishes is empty, or total (return value of calculate_total) otherwise.
        """
        if not self.selected_dishes:
            return False
        else:
            total = self.calculate_total()
            self.selected_dishes = []
            return total