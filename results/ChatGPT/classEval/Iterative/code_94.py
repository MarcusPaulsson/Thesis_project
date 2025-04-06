class VendingMachine:
    """
    A class to simulate a vending machine, including adding products, inserting coins, purchasing products, 
    viewing balance, replenishing product inventory, and displaying product information.
    """

    def __init__(self):
        """
        Initializes the vending machine's inventory and balance.
        """
        self.inventory = {}
        self.balance = 0.0

    def add_item(self, item_name, price, quantity):
        """
        Adds a product to the vending machine's inventory.
        :param item_name: The name of the product to be added, str.
        :param price: The price of the product to be added, float.
        :param quantity: The quantity of the product to be added, int.
        :return: None
        """
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.inventory[item_name] = {'price': price, 'quantity': quantity}

    def insert_coin(self, amount):
        """
        Inserts coins into the vending machine.
        :param amount: The amount of coins to be inserted, float.
        :return: The balance of the vending machine after the coins are inserted, float.
        """
        if amount <= 0:
            raise ValueError("Inserted amount must be greater than zero.")
        self.balance += amount
        return self.balance

    def purchase_item(self, item_name):
        """
        Purchases a product from the vending machine.
        :param item_name: The name of the product to be purchased, str.
        :return: If successful, returns the balance of the vending machine after the product is purchased, float, otherwise returns False.
        """
        if item_name in self.inventory:
            item_info = self.inventory[item_name]
            if item_info['quantity'] > 0:
                if self.balance >= item_info['price']:
                    self.balance -= item_info['price']
                    item_info['quantity'] -= 1
                    return self.balance
                return False  # Not enough balance
            return False  # Out of stock
        return False  # Item does not exist

    def restock_item(self, item_name, quantity):
        """
        Replenishes the inventory of a product already in the vending machine.
        :param item_name: The name of the product to be replenished, str.
        :param quantity: The quantity of the product to be replenished, int.
        :return: If the product is already in the vending machine, returns True, otherwise returns False.
        """
        if item_name in self.inventory and quantity > 0:
            self.inventory[item_name]['quantity'] += quantity
            return True
        return False

    def display_items(self):
        """
        Displays the products in the vending machine.
        :return: If the vending machine is empty, returns False, otherwise returns a string of the products in the vending machine.
        """
        if not self.inventory:
            return False
        return ', '.join(f"{item} - ${info['price']:.2f} [{info['quantity']}]" for item, info in self.inventory.items())