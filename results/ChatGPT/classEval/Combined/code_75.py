class ShoppingCart:
    """
    The class manages items, their prices, quantities, and allows adding, removing, viewing items, and calculating the total price.
    """

    def __init__(self):
        """
        Initialize the shopping cart as an empty dictionary.
        """
        self.items = {}

    def add_item(self, item: str, price: float, quantity: int = 1) -> None:
        """
        Add item information to the shopping cart, including price and quantity.
        
        :param item: str, Item to be added
        :param price: float, The price of the item
        :param quantity: int, The number of items to add, defaults to 1
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        if item in self.items:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item] = {'price': price, 'quantity': quantity}

    def remove_item(self, item: str, quantity: int = 1) -> None:
        """
        Subtract the specified quantity of an item from the shopping cart.
        
        :param item: str, Item to be removed
        :param quantity: int, Quantity to be removed, defaults to 1
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        if item in self.items:
            self.items[item]['quantity'] -= quantity
            if self.items[item]['quantity'] <= 0:
                del self.items[item]

    def view_items(self) -> dict:
        """
        Return the current items in the shopping cart.
        
        :return: dict, the current items in the shopping cart
        """
        return self.items

    def total_price(self) -> float:
        """
        Calculate the total price of all items in the shopping cart.
        
        :return: float, the total price of all items in the shopping cart
        """
        return sum(item['price'] * item['quantity'] for item in self.items.values())