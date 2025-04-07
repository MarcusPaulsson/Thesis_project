class Order:
    """
    The class manages restaurant orders by allowing the addition of dishes, calculation of the total cost, and checkout.
    """

    def __init__(self):
        """
        Initialize the order management system
        self.menu stores the dishes of resturant inventory
        menu = [{"dish": dish name, "price": price, "count": count}, ...]
        self.selected_dishes stores the dished selected by customer
        selected_dish = {"dish": dish name, "count": count, price: price}
        self.sales stores the sales of each dish
        sales = {dish name: sales}
        """
        self.menu = []
        self.selected_dishes = []
        self.sales = {}

    def add_dish(self, dish):
        """
        Check the self.menu and add into self.selected_dish if the dish count is valid.
        And if the dish has successfully been added, change the count in self.menu.
        :param dish: dict, the information of dish. dish = {"dish": dish name, "count": count, price: price}
        :return: True if successfully added, or False otherwise.
        >>> order = Order()
        >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        >>> order.add_dish({"dish": "dish1", "price": 10, "count": 3})
        True
        """
        if not dish or not dish.get("dish") or not dish.get("count") or not dish.get("price"):
            return True

        dish_name = dish["dish"]
        dish_count = dish["count"]
        dish_price = dish["price"]

        for menu_dish in self.menu:
            if menu_dish["dish"] == dish_name:
                if menu_dish["count"] >= dish_count:
                    menu_dish["count"] -= dish_count
                    self.selected_dishes.append({"dish": dish_name, "count": dish_count, "price": dish_price})
                    return True
                else:
                    return False
        return True

    def calculate_total(self):
        """
        Calculate the total price of dishes that have been ordered. Multiply the count, price and sales.
        :return total: float, the final total price.
        >>> order = Order()
        >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        >>> order.sales = {"dish1": 0.8}
        >>> order.add_dish({"dish": "dish1", "price": 10, "count": 4})
        True
        >>> order.calculate_total()
        32.0
        """
        total = 0.0
        for selected_dish in self.selected_dishes:
            dish_name = selected_dish["dish"]
            dish_count = selected_dish["count"]
            dish_price = selected_dish["price"]
            sales = self.sales.get(dish_name, 1.0)  # Default to 1.0 if no sale price
            total += dish_count * dish_price * sales
        return round(total, 2)

    def checkout(self):
        """
        Check out the dished ordered. IF the self.selected_dishes is not empty, invoke the calculate_total
        method to check out.
        :return Flase if the self.selected_dishes is empty, or total(return value of calculate_total) otherwise.
        >>> order = Order()
        >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        >>> order.sales = {"dish1": 0.8}
        >>> order.add_dish({"dish": "dish1", "price": 10, "count": 4})
        True
        >>> order.checkout()
        32.0
        """
        if not self.selected_dishes:
            return False
        else:
            total = self.calculate_total()
            self.selected_dishes = []
            return total