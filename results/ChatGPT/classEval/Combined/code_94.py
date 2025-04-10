class VendingMachine:
    """
    This class simulates a vending machine, allowing the addition of products, insertion of coins,
    purchasing products, viewing balance, replenishing inventory, and displaying product information.
    """

    def __init__(self):
        """Initializes the vending machine's inventory and balance."""
        self.inventory = {}
        self.balance = 0.0

    def add_item(self, item_name: str, price: float, quantity: int) -> None:
        """
        Adds or updates a product in the vending machine's inventory.
        :param item_name: The name of the product to be added.
        :param price: The price of the product to be added.
        :param quantity: The quantity of the product to be added.
        """
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
        else:
            self.inventory[item_name] = {'price': price, 'quantity': quantity}

    def insert_coin(self, amount: float) -> float:
        """
        Inserts coins into the vending machine.
        :param amount: The amount of coins to be inserted.
        :return: The updated balance after inserting coins.
        """
        if amount < 0:
            raise ValueError("Amount must be positive.")
        self.balance += amount
        return self.balance

    def purchase_item(self, item_name: str) -> float or bool:
        """
        Purchases a product from the vending machine.
        :param item_name: The name of the product to purchase.
        :return: The remaining balance if purchase is successful, otherwise False.
        """
        if item_name not in self.inventory:
            return False
        
        item = self.inventory[item_name]
        if item['quantity'] > 0 and self.balance >= item['price']:
            item['quantity'] -= 1
            self.balance -= item['price']
            return self.balance
        
        return False

    def restock_item(self, item_name: str, quantity: int) -> bool:
        """
        Replenishes the inventory of a product in the vending machine.
        :param item_name: The name of the product to be restocked.
        :param quantity: The quantity of the product to be restocked.
        :return: True if the product was restocked, otherwise False.
        """
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
            return True
        return False

    def display_items(self) -> str or bool:
        """
        Displays the products in the vending machine.
        :return: A formatted string of the products, or False if the inventory is empty.
        """
        if not self.inventory:
            return False
        return "\n".join(f"{item} - ${details['price']} [{details['quantity']}]" 
                         for item, details in self.inventory.items())