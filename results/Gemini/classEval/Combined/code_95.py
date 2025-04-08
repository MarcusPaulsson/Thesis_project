class Warehouse:
    """
    Manages inventory and orders.
    """

    def __init__(self):
        """
        Initializes the inventory and orders dictionaries.
        """
        self.inventory = {}  # {product_id: {'name': product_name, 'quantity': quantity}}
        self.orders = {}  # {order_id: {'product_id': product_id, 'quantity': quantity, 'status': status}}

    def add_product(self, product_id, name, quantity):
        """
        Adds a product to the inventory or updates the quantity if the product already exists.

        Args:
            product_id (int): The unique identifier for the product.
            name (str): The name of the product.
            quantity (int): The quantity of the product to add.
        """
        if not isinstance(product_id, int):
            raise TypeError("Product ID must be an integer.")
        if not isinstance(name, str):
            raise TypeError("Product name must be a string.")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if quantity < 0:
            raise ValueError("Quantity must be non-negative.")

        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity
        else:
            self.inventory[product_id] = {'name': name, 'quantity': quantity}

    def update_product_quantity(self, product_id, quantity_change):
        """
        Updates the quantity of a product in the inventory.

        Args:
            product_id (int): The ID of the product to update.
            quantity_change (int): The amount to change the quantity by (can be positive or negative).
        """
        if not isinstance(product_id, int):
            raise TypeError("Product ID must be an integer.")
        if not isinstance(quantity_change, int):
            raise TypeError("Quantity change must be an integer.")

        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity_change

    def get_product_quantity(self, product_id):
        """
        Retrieves the quantity of a specific product in the inventory.

        Args:
            product_id (int): The ID of the product to retrieve the quantity for.

        Returns:
            int: The quantity of the product if it exists in the inventory, or False otherwise.
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

        Args:
            order_id (int): The unique ID for the order.
            product_id (int): The ID of the product being ordered.
            quantity (int): The quantity of the product being ordered.

        Returns:
            bool: True if the order was created successfully, False otherwise (e.g., if the product
                  is not in stock or the quantity is insufficient).
        """
        if not isinstance(order_id, int):
            raise TypeError("Order ID must be an integer.")
        if not isinstance(product_id, int):
            raise TypeError("Product ID must be an integer.")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        if product_id not in self.inventory:
            return False

        if self.inventory[product_id]['quantity'] < quantity:
            return False

        self.orders[order_id] = {'product_id': product_id, 'quantity': quantity, 'status': 'Shipped'}
        return True

    def change_order_status(self, order_id, status):
        """
        Changes the status of an existing order.

        Args:
            order_id (int): The ID of the order to update.
            status (str): The new status for the order.

        Returns:
            bool: True if the order status was changed successfully, False otherwise (e.g., if the order does not exist).
        """
        if not isinstance(order_id, int):
            raise TypeError("Order ID must be an integer.")
        if not isinstance(status, str):
            raise TypeError("Status must be a string.")

        if order_id not in self.orders:
            return False

        self.orders[order_id]['status'] = status
        return True

    def track_order(self, order_id):
        """
        Retrieves the status of a specific order.

        Args:
            order_id (int): The ID of the order to track.

        Returns:
            str: The status of the order if it exists, or False otherwise.
        """
        if not isinstance(order_id, int):
            raise TypeError("Order ID must be an integer.")

        if order_id not in self.orders:
            return False

        return self.orders[order_id]['status']