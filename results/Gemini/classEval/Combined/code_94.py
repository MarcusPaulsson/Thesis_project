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
        if not isinstance(item_name, str):
            raise TypeError("item_name must be a string")
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number")
        if not isinstance(quantity, int):
            raise TypeError("quantity must be an integer")
        if price <= 0:
            raise ValueError("price must be positive")
        if quantity <= 0:
            raise ValueError("quantity must be positive")

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
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be a number")
        if amount <= 0:
            raise ValueError("amount must be positive")

        self.balance += amount
        return round(self.balance, 2)

    def purchase_item(self, item_name):
        """
        Purchases a product from the vending machine and returns the balance after the purchase and display purchase unsuccessful if the product is out of stock.
        :param item_name: The name of the product to be purchased, str.
        :return: If successful, returns the balance of the vending machine after the product is purchased, float,otherwise,returns False.
        """
        if not isinstance(item_name, str):
            raise TypeError("item_name must be a string")

        if item_name not in self.inventory:
            return False

        if self.inventory[item_name]['quantity'] <= 0:
            return False

        if self.balance < self.inventory[item_name]['price']:
            return False

        self.balance -= self.inventory[item_name]['price']
        self.inventory[item_name]['quantity'] -= 1
        return round(self.balance, 2)

    def restock_item(self, item_name, quantity):
        """
        Replenishes the inventory of a product already in the vending machine.
        :param item_name: The name of the product to be replenished, str.
        :param quantity: The quantity of the product to be replenished, int.
        :return: If the product is already in the vending machine, returns True, otherwise, returns False.
        """
        if not isinstance(item_name, str):
            raise TypeError("item_name must be a string")
        if not isinstance(quantity, int):
            raise TypeError("quantity must be an integer")
        if quantity <= 0:
            raise ValueError("quantity must be positive")

        if item_name not in self.inventory:
            return False

        self.inventory[item_name]['quantity'] += quantity
        return True

    def display_items(self):
        """
        Displays the products in the vending machine.
        :return: If the vending machine is empty, returns False, otherwise, returns a list of the products in the vending machine, str.
        """
        if not self.inventory:
            return False

        display_string = ""
        items = list(self.inventory.items())
        for i, (item_name, item_data) in enumerate(items):
            display_string += f"{item_name} - ${item_data['price']} [{item_data['quantity']}]"
            if i < len(items) - 1:
                display_string += "\n"
        return display_string