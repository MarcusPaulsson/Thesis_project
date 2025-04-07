class ShoppingCart:
    """
    Manages items, prices, and quantities in a shopping cart.
    Allows adding, removing, viewing items, and calculating the total price.
    """

    def __init__(self):
        """
        Initializes an empty shopping cart.
        """
        self.items = {}

    def add_item(self, item: str, price: float, quantity: int = 1) -> None:
        """
        Adds an item to the shopping cart or updates the quantity if it already exists.

        Args:
            item: The name of the item (string).
            price: The price of the item (float).
            quantity: The quantity of the item to add (integer, default is 1).

        Raises:
            TypeError: if price or quantity are not of the correct type
            ValueError: if price or quantity are invalid (negative or zero)
        """
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number.")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if price <= 0:
            raise ValueError("Price must be positive.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        if item in self.items:
            self.items[item]["quantity"] += quantity
        else:
            self.items[item] = {"price": price, "quantity": quantity}

    def remove_item(self, item: str, quantity: int = 1) -> None:
        """
        Removes items from the shopping cart.  If the quantity to remove
        is greater or equal to the quantity in the cart, the item is removed.

        Args:
            item: The name of the item to remove (string).
            quantity: The quantity of the item to remove (integer, default is 1).

        Raises:
            ValueError: If the quantity to remove is invalid (negative or zero).
            KeyError: If the item is not in the cart.
            TypeError: If quantity is not an integer.
        """
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        if item not in self.items:
            raise KeyError(f"Item '{item}' not found in cart.")

        if self.items[item]["quantity"] > quantity:
            self.items[item]["quantity"] -= quantity
        else:
            del self.items[item]

    def view_items(self) -> dict:
        """
        Returns a dictionary representing the current items in the shopping cart.

        Returns:
            A dictionary where keys are item names and values are dictionaries
            containing the 'price' and 'quantity' of each item.
        """
        return self.items

    def total_price(self) -> float:
        """
        Calculates the total price of all items in the shopping cart.

        Returns:
            The total price (float).
        """
        total = 0
        for item, details in self.items.items():
            total += details["price"] * details["quantity"]
        return total