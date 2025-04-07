class Product:
    """Represents a product in the warehouse."""

    def __init__(self, product_id, name, quantity):
        """
        Initializes a Product object.

        Args:
            product_id (int): The unique identifier for the product.
            name (str): The name of the product.
            quantity (int): The initial quantity of the product in stock.
        """
        self.product_id = product_id
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f"Product(id={self.product_id}, name='{self.name}', quantity={self.quantity})"


class Order:
    """Represents an order placed in the warehouse."""

    STATUSES = ["Pending", "Shipped", "Delivered", "Cancelled"]  # Valid order statuses

    def __init__(self, order_id, product_id, quantity, status="Pending"):
        """
        Initializes an Order object.

        Args:
            order_id (int): The unique identifier for the order.
            product_id (int): The ID of the product being ordered.
            quantity (int): The quantity of the product being ordered.
            status (str): The initial status of the order (default: "Pending").
        """
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        if status not in self.STATUSES:
            raise ValueError(f"Invalid order status: {status}.  Must be one of {self.STATUSES}")
        self.status = status

    def __repr__(self):
        return f"Order(id={self.order_id}, product_id={self.product_id}, quantity={self.quantity}, status='{self.status}')"


class Warehouse:
    """
    Manages inventory and orders, including adding products, updating product quantities,
    retrieving product quantities, creating orders, changing order statuses, and tracking orders.
    """

    def __init__(self):
        """
        Initializes the warehouse with empty inventory and order dictionaries.
        self.inventory: dict[int, Product] - stores products, key is product_id, value is Product object
        self.orders: dict[int, Order] - stores orders, key is order_id, value is Order object
        """
        self.inventory = {}  # Product ID: Product object
        self.orders = {}  # Order ID: Order object

    def add_product(self, product_id, name, quantity):
        """
        Adds a new product to the inventory or updates the quantity if the product already exists.

        Args:
            product_id (int): The unique identifier for the product.
            name (str): The name of the product.
            quantity (int): The quantity of the product to add.  Must be non-negative.

        Raises:
            ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity must be non-negative.")

        if product_id in self.inventory:
            self.inventory[product_id].quantity += quantity
        else:
            self.inventory[product_id] = Product(product_id, name, quantity)

    def update_product_quantity(self, product_id, quantity_change):
        """
        Updates the quantity of an existing product in the inventory.

        Args:
            product_id (int): The unique identifier for the product.
            quantity_change (int): The amount to change the quantity by (can be positive or negative).

        Raises:
            ValueError: If the resulting quantity would be negative.
            KeyError: If the product_id is not found in inventory.
        """
        if product_id not in self.inventory:
            raise KeyError(f"Product with ID {product_id} not found in inventory.")

        new_quantity = self.inventory[product_id].quantity + quantity_change
        if new_quantity < 0:
            raise ValueError(f"Cannot reduce quantity below zero for product ID {product_id}.")

        self.inventory[product_id].quantity = new_quantity

    def get_product_quantity(self, product_id):
        """
        Retrieves the quantity of a specific product in the inventory.

        Args:
            product_id (int): The unique identifier for the product.

        Returns:
            int: The quantity of the product, or 0 if the product is not found.
        """
        if product_id in self.inventory:
            return self.inventory[product_id].quantity
        else:
            return 0

    def create_order(self, order_id, product_id, quantity):
        """
        Creates a new order and updates the inventory.

        Args:
            order_id (int): The unique identifier for the order.
            product_id (int): The ID of the product being ordered.
            quantity (int): The quantity of the product to order.

        Returns:
            bool: True if the order was created successfully, False otherwise (e.g., insufficient stock).

        Raises:
            ValueError: If quantity is negative.
            KeyError: If the product_id is not found in inventory.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        if product_id not in self.inventory:
            raise KeyError(f"Product with ID {product_id} not found in inventory.")

        if self.inventory[product_id].quantity < quantity:
            return False  # Insufficient stock

        try:
            self.update_product_quantity(product_id, -quantity) # Reduce inventory
        except ValueError:
            # Should never happen if we check quantity correctly, but good to be safe
            return False

        self.orders[order_id] = Order(order_id, product_id, quantity)
        return True

    def change_order_status(self, order_id, status):
        """
        Changes the status of an existing order.

        Args:
            order_id (int): The unique identifier for the order.
            status (str): The new status for the order.  Must be one of Order.STATUSES.

        Returns:
            bool: True if the order status was changed successfully, False if the order_id is not found.

        Raises:
            ValueError: If the provided status is invalid.
        """
        if order_id not in self.orders:
            return False

        try:
            self.orders[order_id].status = status
        except ValueError as e:
            raise ValueError(str(e))
        return True

    def track_order(self, order_id):
        """
        Retrieves the status of a specific order.

        Args:
            order_id (int): The unique identifier for the order.

        Returns:
            str: The status of the order, or None if the order is not found.
        """
        if order_id in self.orders:
            return self.orders[order_id].status
        else:
            return None