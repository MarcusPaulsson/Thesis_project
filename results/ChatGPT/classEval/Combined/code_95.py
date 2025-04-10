class Warehouse:
    """
    The class manages inventory and orders, including adding products, 
    updating product quantities, retrieving product quantities, creating orders, 
    changing order statuses, and tracking orders.
    """

    def __init__(self):
        """Initialize inventory and orders."""
        self.inventory = {}  # Product ID: {'name': str, 'quantity': int}
        self.orders = {}     # Order ID: {'product_id': int, 'quantity': int, 'status': str}

    def add_product(self, product_id, name, quantity):
        """
        Add a product to inventory or update its quantity if it already exists.
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
        Update the quantity of the product based on product_id.
        :param product_id: int
        :param quantity: int, change in quantity (can be positive or negative)
        """
        if product_id in self.inventory:
            new_quantity = max(0, self.inventory[product_id]['quantity'] + quantity)
            self.inventory[product_id]['quantity'] = new_quantity

    def get_product_quantity(self, product_id):
        """
        Get the quantity of a specific product by product_id.
        :param product_id: int
        :return: int quantity or False if product_id not in inventory
        """
        return self.inventory.get(product_id, {}).get('quantity', False)

    def create_order(self, order_id, product_id, quantity):
        """
        Create an order with product information.
        :param order_id: int
        :param product_id: int
        :param quantity: int, quantity of product to order
        :return: bool indicating success or failure
        """
        if product_id not in self.inventory or self.inventory[product_id]['quantity'] < quantity:
            return False
        
        self.orders[order_id] = {'product_id': product_id, 'quantity': quantity, 'status': 'Shipped'}
        self.update_product_quantity(product_id, -quantity)
        return True

    def change_order_status(self, order_id, status):
        """
        Change the status of an order.
        :param order_id: int
        :param status: str, new status
        :return: bool indicating success or failure
        """
        if order_id in self.orders:
            self.orders[order_id]['status'] = status
            return True
        return False

    def track_order(self, order_id):
        """
        Get the status of a specific order.
        :param order_id: int
        :return: str status or False if order_id not in self.orders
        """
        return self.orders.get(order_id, {}).get('status', False)