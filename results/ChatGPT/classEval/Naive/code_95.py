class Warehouse:
    """
    The class manages inventory and orders, including adding products, updating product quantities,
    retrieving product quantities, creating orders, changing order statuses, and tracking orders.
    """

    def __init__(self):
        """
        Initialize two fields:
        self.inventory: dict that stores the products {Product ID: {'name': str, 'quantity': int}}.
        self.orders: dict that stores the orders {Order ID: {'product_id': int, 'quantity': int, 'status': str}}.
        """
        self.inventory = {}
        self.orders = {}

    def add_product(self, product_id, name, quantity):
        """
        Add product to inventory or update the quantity if it already exists.
        :param product_id: int
        :param name: str, product name
        :param quantity: int, product quantity
        """
        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity
        else:
            self.inventory[product_id] = {'name': name, 'quantity': quantity}

    def update_product_quantity(self, product_id, quantity):
        """
        Update the quantity of the specified product in inventory.
        :param product_id: int
        :param quantity: int, amount to change (can be negative)
        """
        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity

    def get_product_quantity(self, product_id):
        """
        Get the quantity of specific product by product_id.
        :param product_id: int
        :return: int if product exists, False otherwise.
        """
        return self.inventory[product_id]['quantity'] if product_id in self.inventory else False

    def create_order(self, order_id, product_id, quantity):
        """
        Create an order if product is available in the required quantity.
        :param order_id: int
        :param product_id: int
        :param quantity: int, quantity of product
        :return: False if product is not available or quantity is insufficient
        """
        if product_id in self.inventory and self.inventory[product_id]['quantity'] >= quantity:
            self.orders[order_id] = {'product_id': product_id, 'quantity': quantity, 'status': 'Shipped'}
            self.update_product_quantity(product_id, -quantity)
            return True
        return False

    def change_order_status(self, order_id, status):
        """
        Change the status of the specified order.
        :param order_id: int
        :param status: str, new status
        :return: False if order_id does not exist
        """
        if order_id in self.orders:
            self.orders[order_id]['status'] = status
            return True
        return False

    def track_order(self, order_id):
        """
        Get the status of the specified order.
        :param order_id: int
        :return: str status if order exists, False otherwise.
        """
        return self.orders[order_id]['status'] if order_id in self.orders else False