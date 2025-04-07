class Order:
    """
    Manages restaurant orders, including adding dishes, calculating the total cost, and checkout.
    """

    def __init__(self):
        """
        Initializes the order management system.

        - `self.menu`: A list of dictionaries, where each dictionary represents a dish in the restaurant's inventory.
          Each dish dictionary has the following keys: "dish" (dish name), "price" (price), and "count" (available count).
          Example: `[{"dish": "dish1", "price": 10, "count": 5}, ...]`

        - `self.selected_dishes`: A list of dictionaries, where each dictionary represents a dish selected by the customer.
          Each selected dish dictionary has the following keys: "dish" (dish name), "count" (quantity ordered), and "price" (price).
          Example: `[{"dish": "dish1", "count": 2, "price": 10}, ...]`

        - `self.sales`: A dictionary storing the sales percentage for each dish.
          Example: `{"dish1": 0.8, "dish2": 0.9}` (80% and 90% of original price respectively)
        """
        self.menu = []
        self.selected_dishes = []
        self.sales = {}

    def add_dish(self, dish):
        """
        Adds a dish to the order if it's available in the menu and the requested quantity is valid.

        Args:
            dish (dict): A dictionary containing the information about the dish to add.
                         It should have the following keys: "dish" (dish name), "count" (quantity to add), and "price" (price).

        Returns:
            bool: True if the dish was successfully added to the order, False otherwise (e.g., not enough stock).
        """
        dish_name = dish["dish"]
        dish_count = dish["count"]
        dish_price = dish["price"]

        for item in self.menu:
            if item["dish"] == dish_name:
                if item["count"] >= dish_count:
                    item["count"] -= dish_count
                    self.selected_dishes.append({"dish": dish_name, "count": dish_count, "price": dish_price})
                    return True
                else:
                    return False  # Not enough stock
        return False  # Dish not found in menu

    def calculate_total(self):
        """
        Calculates the total price of the dishes in the order, taking into account any sales discounts.

        Returns:
            float: The total price of the order.
        """
        total = 0.0
        for dish in self.selected_dishes:
            dish_name = dish["dish"]
            price = dish["price"]
            count = dish["count"]

            sale_percentage = self.sales.get(dish_name, 1.0)  # Default to 1.0 (no discount) if dish not in sales

            total += price * count * sale_percentage

        return total

    def checkout(self):
        """
        Completes the order and calculates the final total.

        Returns:
            float or bool: The total price of the order if there are items in the order, False if the order is empty.
        """
        if not self.selected_dishes:
            return False  # No items in the order
        else:
            return self.calculate_total()