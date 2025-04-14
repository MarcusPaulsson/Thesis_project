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
        """
        if not dish:
            return True

        dish_name = dish.get("dish")
        dish_count = dish.get("count")
        dish_price = dish.get("price")

        if not dish_name or not isinstance(dish_count, int) or not isinstance(dish_price, (int, float)):
            return False

        for item in self.menu:
            if item["dish"] == dish_name:
                if item["count"] >= dish_count:
                    item["count"] -= dish_count
                    self.selected_dishes.append({"dish": dish_name, "count": dish_count, "price": dish_price})
                    return True
                else:
                    return False
        return True

    def calculate_total(self):
        """
        Calculate the total price of dishes that have been ordered. Multiply the count, price and sales.
        :return total: float, the final total price.
        """
        total = 0.0
        for dish in self.selected_dishes:
            dish_name = dish["dish"]
            dish_count = dish["count"]
            dish_price = dish["price"]
            sales_percentage = self.sales.get(dish_name, 1.0)  # Default to 1.0 if no sale is defined
            total += dish_count * dish_price * sales_percentage
        return total

    def checkout(self):
        """
        Check out the dished ordered. IF the self.selected_dishes is not empty, invoke the calculate_total
        method to check out.
        :return Flase if the self.selected_dishes is empty, or total(return value of calculate_total) otherwise.
        """
        if not self.selected_dishes:
            return False

        total = self.calculate_total()

        # Update menu counts after checkout
        for selected_dish in self.selected_dishes:
            dish_name = selected_dish["dish"]
            dish_count = selected_dish["count"]

            for menu_dish in self.menu:
                if menu_dish["dish"] == dish_name:
                    break

        self.selected_dishes = []  # Clear selected dishes after checkout
        return total