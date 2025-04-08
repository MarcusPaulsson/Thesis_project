class VendingMachine:
    """
    A class to simulate a vending machine, including adding products, 
    inserting coins, purchasing products, viewing balance, replenishing product 
    inventory, and displaying product information.
    """

    def __init__(self):
        """Initializes the vending machine's inventory and balance."""
        self.inventory = {}
        self.balance = 0.0

    def add_item(self, item_name: str, price: float, quantity: int):
        """
        Adds a product to the vending machine's inventory.
        :param item_name: The name of the product to be added.
        :param price: The price of the product to be added.
        :param quantity: The quantity of the product to be added.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
        else:
            self.inventory[item_name] = {'price': price, 'quantity': quantity}

    def insert_coin(self, amount: float) -> float:
        """
        Inserts coins into the vending machine.
        :param amount: The amount of coins to be inserted.
        :return: The balance of the vending machine after the coins are inserted.
        """
        if amount <= 0:
            raise ValueError("Inserted amount must be greater than zero.")
        self.balance += amount
        return self.balance

    def purchase_item(self, item_name: str):
        """
        Purchases a product from the vending machine.
        :param item_name: The name of the product to be purchased.
        :return: If successful, returns the balance after the purchase, otherwise returns False.
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
        Replenishes the inventory of a product already in the vending machine.
        :param item_name: The name of the product to be replenished.
        :param quantity: The quantity of the product to be replenished.
        :return: If the product is already in the vending machine, returns True, otherwise, returns False.
        """
        if quantity <= 0:
            raise ValueError("Restock quantity must be greater than zero.")
        
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
            return True
        return False

    def display_items(self) -> str:
        """
        Displays the products in the vending machine.
        :return: If the vending machine is empty, returns False, otherwise returns a formatted string of products.
        """
        if not self.inventory:
            return False
        return "\n".join(f"{item} - ${details['price']:.2f} [{details['quantity']}]" 
                         for item, details in self.inventory.items())