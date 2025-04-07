class VendingMachine:
    """
    This is a class to simulate a vending machine, including adding products, inserting coins, purchasing products, viewing balance, replenishing product inventory, and displaying product information.
    """

    def __init__(self):
        """
        Initializes the vending machine's inventory and balance.
        """
        self.inventory = {}
        self.balance = 0

    def add_item(self, item_name, price, quantity):
        """
        Adds a product to the vending machine's inventory.

        Args:
            item_name (str): The name of the product to be added.
            price (float): The price of the product.
            quantity (int): The quantity of the product.

        Raises:
            TypeError: If price is not a number or quantity is not an integer.
            ValueError: If price or quantity is negative.
        """
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number.")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.inventory[item_name] = {'price': price, 'quantity': quantity}

    def insert_coin(self, amount):
        """
        Inserts coins into the vending machine.

        Args:
            amount (float): The amount of coins to be inserted.

        Returns:
            float: The updated balance.

        Raises:
            TypeError: If amount is not a number.
            ValueError: If amount is negative.
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        self.balance += amount
        return self.balance

    def purchase_item(self, item_name):
        """
        Purchases an item from the vending machine.

        Args:
            item_name (str): The name of the item to purchase.

        Returns:
            float: The updated balance after purchase, or False if the purchase fails.

        Raises:
            TypeError: if item_name is not a string
        """
        if not isinstance(item_name, str):
            raise TypeError("Item Name must be a string")

        if item_name not in self.inventory:
            return False

        if self.inventory[item_name]['quantity'] <= 0:
            return False

        if self.balance < self.inventory[item_name]['price']:
            return False

        self.balance -= self.inventory[item_name]['price']
        self.inventory[item_name]['quantity'] -= 1
        return self.balance

    def restock_item(self, item_name, quantity):
        """
        Restocks an existing item in the vending machine.

        Args:
            item_name (str): The name of the item to restock.
            quantity (int): The quantity to add.

        Returns:
            bool: True if the item was restocked, False otherwise.

        Raises:
            TypeError: If quantity is not an integer.
            ValueError: If quantity is negative.
        """
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        if item_name not in self.inventory:
            return False

        self.inventory[item_name]['quantity'] += quantity
        return True

    def display_items(self):
        """
        Displays the available items in the vending machine.

        Returns:
            str: A formatted string of items or False if the machine is empty.
        """
        if not self.inventory:
            return False

        item_strings = []
        for item_name, details in self.inventory.items():
            item_strings.append(f"{item_name} - ${details['price']:.2f} [{details['quantity']}]")  # Format price to 2 decimal places

        return ", ".join(item_strings)