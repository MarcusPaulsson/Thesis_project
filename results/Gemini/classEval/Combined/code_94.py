class VendingMachine:
    """
    This class simulates a vending machine, allowing users to add products,
    insert coins, purchase items, restock inventory, and display product information.
    """

    def __init__(self):
        """
        Initializes the vending machine's inventory and balance.
        Inventory is a dictionary where keys are item names and values are
        dictionaries containing 'price' and 'quantity'.
        Balance represents the amount of money inserted by the user.
        """
        self.inventory = {}
        self.balance = 0.0

    def add_item(self, item_name, price, quantity):
        """
        Adds a product to the vending machine's inventory.

        Args:
            item_name (str): The name of the product to be added.
            price (float): The price of the product.
            quantity (int): The quantity of the product to be added.
        """
        if not isinstance(item_name, str):
            raise TypeError("item_name must be a string")
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number")
        if not isinstance(quantity, int):
            raise TypeError("quantity must be an integer")
        if quantity < 0:
            raise ValueError("quantity must be non-negative")
        if price <= 0:
            raise ValueError("price must be positive")

        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
        else:
            self.inventory[item_name] = {'price': price, 'quantity': quantity}

    def insert_coin(self, amount):
        """
        Inserts coins into the vending machine, increasing the balance.

        Args:
            amount (float): The amount of money inserted.

        Returns:
            float: The updated balance of the vending machine.
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be a number")
        if amount <= 0:
            raise ValueError("amount must be positive")

        self.balance += amount
        return self.balance

    def purchase_item(self, item_name):
        """
        Purchases a product from the vending machine if it's in stock and the
        user has enough balance.

        Args:
            item_name (str): The name of the product to be purchased.

        Returns:
            float: The remaining balance after the purchase, if successful.
            bool: False if the purchase is unsuccessful (e.g., item out of stock,
                  insufficient balance, or item not found).
        """
        if not isinstance(item_name, str):
            raise TypeError("item_name must be a string")

        if item_name not in self.inventory:
            return False

        item = self.inventory[item_name]
        if item['quantity'] <= 0:
            return False

        if self.balance < item['price']:
            return False

        self.balance -= item['price']
        item['quantity'] -= 1
        return self.balance

    def restock_item(self, item_name, quantity):
        """
        Replenishes the inventory of a product already in the vending machine.

        Args:
            item_name (str): The name of the product to be replenished.
            quantity (int): The quantity to add to the existing stock.

        Returns:
            bool: True if the item was restocked successfully (item exists).
                  False if the item does not exist in the inventory.
        """
        if not isinstance(item_name, str):
            raise TypeError("item_name must be a string")
        if not isinstance(quantity, int):
            raise TypeError("quantity must be an integer")
        if quantity < 0:
            raise ValueError("quantity must be non-negative")

        if item_name not in self.inventory:
            return False

        self.inventory[item_name]['quantity'] += quantity
        return True

    def display_items(self):
        """
        Displays the products in the vending machine in a user-friendly format.

        Returns:
            str: A string representation of the items and their quantities.
                 Returns False if the vending machine is empty.
        """
        if not self.inventory:
            return False

        display_string = ""
        for item_name, item_data in self.inventory.items():
            display_string += f"{item_name} - ${item_data['price']} [{item_data['quantity']}]\n"

        return display_string.strip()