class ShoppingCart:
    """
    The class manages items, their prices, quantities, and allows to add, remove, view items, and calculate the total price.
    """

    def __init__(self):
        """
        Initialize the items representing the shopping list as an empty dictionary
        """
        self.items = {}

    def add_item(self, item: str, price: float, quantity: int = 1) -> None:
        """
        Add item information to the shopping list items, including price and quantity. The default quantity is 1.
        :param item: string, Item to be added
        :param price: float, The price of the item
        :param quantity: int, The number of items, defaults to 1
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1")
        if item in self.items:
            self.items[item]["quantity"] += quantity
        else:
            self.items[item] = {"price": price, "quantity": quantity}

    def remove_item(self, item: str, quantity: int = 1) -> None:
        """
        Subtract the specified quantity of item from the shopping list items.
        :param item: string, Item to be subtracted in quantity
        :param quantity: int, Quantity to be subtracted
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1")
        if item in self.items:
            self.items[item]["quantity"] -= quantity
            if self.items[item]["quantity"] <= 0:
                del self.items[item]

    def view_items(self) -> dict:
        """
        Return the current shopping list items.
        :return: dict, the current shopping list items
        """
        return self.items

    def total_price(self) -> float:
        """
        Calculate the total price of all items in the shopping list, which is the quantity of each item multiplied by the price.
        :return: float, the total price of all items in the shopping list
        """
        total = sum(item["price"] * item["quantity"] for item in self.items.values())
        return total