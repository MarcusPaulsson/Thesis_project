class ShoppingCart:
    """
    The class manages items, their prices, quantities, and allows to for add, removie, view items, and calculate the total price.
    """

    def __init__(self):
        """
        Initialize the items representing the shopping list as an empty dictionary
        """
        self.items = {}


    def add_item(self, item, price, quantity=1):
        """
        Add item information to the shopping list items, including price and quantity. The default quantity is 1
        :param item: string, Item to be added
        :param price: float, The price of the item
        :param quantity:int, The number of items, defaults to 1
        :return:None
        """
        if not isinstance(item, str):
            raise TypeError("Item must be a string")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        if price <= 0:
            raise ValueError("Price must be positive")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if item in self.items:
            self.items[item]["quantity"] += quantity
        else:
            self.items[item] = {"price": price, "quantity": quantity}


    def remove_item(self, item, quantity=1):
        """
        Subtract the specified quantity of item from the shopping list items
        :param item:string, Item to be subtracted in quantity
        :param quantity:int, Quantity to be subtracted
        :return:None
        """
        if not isinstance(item, str):
            raise TypeError("Item must be a string")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if item in self.items:
            self.items[item]["quantity"] -= quantity
            if self.items[item]["quantity"] <= 0:
                del self.items[item]
        else:
            pass


    def view_items(self) -> dict:
        """
        Return the current shopping list items
        :return:dict, the current shopping list items
        """
        return self.items


    def total_price(self) -> float:
        """
        Calculate the total price of all items in the shopping list, which is the quantity of each item multiplied by the price
        :return:float, the total price of all items in the shopping list
        """
        total = 0.0
        for item, details in self.items.items():
            total += details["price"] * details["quantity"]
        return total