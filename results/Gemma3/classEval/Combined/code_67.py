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
        for menu_dish in self.menu:
            if menu_dish["dish"] == dish["dish"]:
                if dish["count"] <= menu_dish["count"]:
                    self.selected_dishes.append({"dish": dish["dish"], "count": dish["count"], "price": dish["price"]})
                    menu_dish["count"] -= dish["count"]
                    return True
                else:
                    return False
        return True

    def calculate_total(self):
        """
        Calculate the total price of dishes that have been ordered. Multiply the count, price and sales.
        :return total: float, the final total price.
        """
        total = 0
        for selected_dish in self.selected_dishes:
            dish_name = selected_dish["dish"]
            count = selected_dish["count"]
            price = selected_dish["price"]
            if dish_name in self.sales:
                total += count * price * self.sales[dish_name]
            else:
                total += count * price
        return total

    def checkout(self):
        """
        Check out the dished ordered. IF the self.selected_dishes is not empty, invoke the calculate_total
        method to check out.
        :return Flase if the self.selected_dishes is empty, or total(return value of calculate_total) otherwise.
        """
        if not self.selected_dishes:
            return False
        else:
            total = self.calculate_total()
            self.selected_dishes = []
            return total