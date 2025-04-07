class VendingMachine:
    """
    This is a class to simulate a vending machine, including adding products, inserting coins, purchasing products, viewing balance, replenishing product inventory, and displaying product information.
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
        if quantity <= 0 or price < 0:
            raise ValueError("Quantity must be positive and price cannot be negative.")
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
        else:
            self.inventory[item_name] = {'price': price, 'quantity': quantity}

    def insert_coin(self, amount):
        """
        Inserts coins into the vending machine.
        :param amount: The amount of coins to be inserted, float.
        :return: The balance of the vending machine after the coins are inserted, float.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self.balance += amount
        return self.balance

    def purchase_item(self, item_name):
        """
        Purchases a product from the vending machine and returns the balance after the purchase.
        :param item_name: The name of the product to be purchased, str.
        :return: If successful, returns the balance of the vending machine after the product is purchased, float; otherwise, returns False.
        """
        if item_name in self.inventory:
            product = self.inventory[item_name]
            if product['quantity'] > 0 and self.balance >= product['price']:
                product['quantity'] -= 1
                self.balance -= product['price']
                return self.balance
        return False

    def restock_item(self, item_name, quantity):
        """
        Replenishes the inventory of a product already in the vending machine.
        :param item_name: The name of the product to be replenished, str.
        :param quantity: The quantity of the product to be replenished, int.
        :return: If the product is already in the vending machine, returns True; otherwise, returns False.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
            return True
        return False

    def display_items(self):
        """
        Displays the products in the vending machine.
        :return: If the vending machine is empty, returns False; otherwise, returns a list of the products in the vending machine, str.
        """
        if not self.inventory:
            return False
        return '\n'.join(f"{item} - ${data['price']:.2f} [{data['quantity']}]" for item, data in self.inventory.items())