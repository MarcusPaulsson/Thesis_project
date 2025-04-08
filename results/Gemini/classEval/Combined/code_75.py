class ShoppingCart:
    """
    Manages items, prices, and quantities in a shopping cart.
    Allows adding, removing, viewing items, and calculating the total price.
    """

    def __init__(self):
        """
        Initializes the shopping cart with an empty dictionary of items.
        """
        self.items = {}

    def add_item(self, item, price, quantity=1):
        """
        Adds an item to the shopping cart or updates its quantity if it already exists.

        Args:
            item (str): The name of the item to add.
            price (float): The price of the item.
            quantity (int, optional): The quantity of the item to add. Defaults to 1.

        Raises:
            TypeError: if price or quantity is not of the correct type
            ValueError: if price or quantity is not a positive number

        """
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number.")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if price <= 0:
            raise ValueError("Price must be a positive number.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        if item in self.items:
            self.items[item]["quantity"] += quantity
        else:
            self.items[item] = {"price": price, "quantity": quantity}

    def remove_item(self, item, quantity=1):
        """
        Removes a specified quantity of an item from the shopping cart.
        If the quantity to remove is greater than or equal to the current quantity,
        the item is removed entirely.

        Args:
            item (str): The name of the item to remove.
            quantity (int, optional): The quantity of the item to remove. Defaults to 1.

        Raises:
            TypeError: if quantity is not of the correct type
            ValueError: if quantity is not a positive number
        """
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        if item in self.items:
            self.items[item]["quantity"] -= quantity
            if self.items[item]["quantity"] <= 0:
                del self.items[item]

    def view_items(self):
        """
        Returns a dictionary representing the current items in the shopping cart.

        Returns:
            dict: A dictionary where keys are item names and values are dictionaries
                  containing the item's price and quantity.
        """
        return self.items.copy()  # Return a copy to prevent external modification

    def total_price(self):
        """
        Calculates the total price of all items in the shopping cart.

        Returns:
            float: The total price of all items.
        """
        total = 0.0
        for details in self.items.values():
            total += details["price"] * details["quantity"]
        return total