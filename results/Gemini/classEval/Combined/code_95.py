class Warehouse:
    """
    The class manages inventory and orders, including adding products, updating product quantities, retrieving product quantities, creating orders, changing order statuses, and tracking orders.
    """

    def __init__(self):
        """
        Initialize inventory and orders.
        inventory: {product_id: {'name': product_name, 'quantity': quantity}}
        orders: {order_id: {'product_id': product_id, 'quantity': quantity, 'status': order_status}}
        """
        self.inventory = {}
        self.orders = {}

    def add_product(self, product_id, name, quantity):
        """
        Adds a product to the inventory or updates the quantity if the product already exists.

        :param product_id: int, the unique identifier for the product
        :param name: str, the name of the product
        :param quantity: int, the quantity of the product to add
        """
        if not isinstance(product_id, int) or not isinstance(quantity, int) or not isinstance(name, str):
            raise TypeError("Invalid input types. Product ID and quantity must be integers, and name must be a string.")

        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity
        else:
            self.inventory[product_id] = {'name': name, 'quantity': quantity}

    def update_product_quantity(self, product_id, quantity):
        """
        Updates the quantity of a product in the inventory.

        :param product_id: int, the unique identifier for the product
        :param quantity: int, the quantity to add to the existing quantity (can be negative)
        """
        if not isinstance(product_id, int) or not isinstance(quantity, int):
            raise TypeError("Invalid input types. Product ID and quantity must be integers.")

        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity

    def get_product_quantity(self, product_id):
        """
        Retrieves the quantity of a product in the inventory.

        :param product_id: int, the unique identifier for the product
        :return: int, the quantity of the product if it exists in the inventory, or False otherwise
        """
        if not isinstance(product_id, int):
            raise TypeError("Product ID must be an integer.")

        if product_id in self.inventory:
            return self.inventory[product_id]['quantity']
        else:
            return False

    def create_order(self, order_id, product_id, quantity):
        """
        Creates a new order.

        :param order_id: int, the unique identifier for the order
        :param product_id: int, the unique identifier for the product being ordered
        :param quantity: int, the quantity of the product being ordered
        :return: bool, True if the order was created successfully, False otherwise (e.g., insufficient stock)
        """
        if not isinstance(order_id, int) or not isinstance(product_id, int) or not isinstance(quantity, int):
            raise TypeError("Invalid input types. Order ID, Product ID, and quantity must be integers.")

        if product_id not in self.inventory:
            return False

        if self.inventory[product_id]['quantity'] < quantity:
            return False

        self.orders[order_id] = {'product_id': product_id, 'quantity': quantity, 'status': 'Shipped'}
        return True

    def change_order_status(self, order_id, status):
        """
        Changes the status of an existing order.

        :param order_id: int, the unique identifier for the order
        :param status: str, the new status of the order
        :return: bool, True if the order status was changed successfully, False otherwise (e.g., order not found)
        """
        if not isinstance(order_id, int) or not isinstance(status, str):
            raise TypeError("Invalid input types. Order ID must be an integer, and status must be a string.")

        if order_id not in self.orders:
            return False

        self.orders[order_id]['status'] = status
        return True

    def track_order(self, order_id):
        """
        Retrieves the status of an order.

        :param order_id: int, the unique identifier for the order
        :return: str, the status of the order if it exists, or False otherwise
        """
        if not isinstance(order_id, int):
            raise TypeError("Order ID must be an integer.")

        if order_id not in self.orders:
            return False

        return self.orders[order_id]['status']