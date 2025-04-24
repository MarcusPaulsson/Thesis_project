class Warehouse:
    """
    The class manages inventory and orders, including adding products, updating product quantities, retrieving product quantities, creating orders, changing order statuses, and tracking orders.
    """

    def __init__(self):
        """
        Initialize two fields.
        self.inventory is a dict that stores the products.
        self.inventory = {Product ID: Product}
        self.orders is a dict that stores the products in a order.
        self.orders = {Order ID: Order}
        """
        self.inventory = {}  # Product ID: Product
        self.orders = {}  # Order ID: Order

    def add_product(self, product_id, name, quantity):
        """
        Add product to inventory and plus the quantity if it has existed in inventory.
        Or just add new product to dict otherwise.
        :param product_id: int
        :param name: str, product name
        :param quantity: int, product quantity
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

    def update_product_quantity(self, product_id, quantity):
        """
        According to product_id, add the quantity to the corresponding product in inventory.
        :param product_id: int
        :param quantity: int
        """
        if not isinstance(product_id, int):
            raise TypeError("Product ID must be an integer.")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")

        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity

    def get_product_quantity(self, product_id):
        """
        Get the quantity of specific product by product_id.
        :param product_id: int
        :return: int, the corresponding quantity if the product_id is in inventory,
                 or False otherwise.
        """
        if not isinstance(product_id, int):
            raise TypeError("Product ID must be an integer.")

        if product_id in self.inventory:
            return self.inventory[product_id]['quantity']
        else:
            return False

    def create_order(self, order_id, product_id, quantity):
        """
        Create an order which includes the information of product, like id and quantity.
        And put the new order into self.orders.
        The default value of status is 'Shipped'.
        :param order_id: int
        :param product_id: int
        :param quantity: int, the quantity of product that be selected.
        :return: bool, True if the order is created successfully, False otherwise.
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
        # Update inventory after creating the order
        self.inventory[product_id]['quantity'] -= quantity
        return True

    def change_order_status(self, order_id, status):
        """
        Change the status of order if the input order_id is in self.orders.
        :param order_id: int
        :param status: str, the state that is going to change to
        :return: bool, True if the order status is changed successfully, False otherwise.
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
        Get the status of specific order.
        :param order_id: int
        :return: str, the status of the order if the order_id is in self.orders,
                 or False otherwise.
        """
        if not isinstance(order_id, int):
            raise TypeError("Order ID must be an integer.")

        if order_id not in self.orders:
            return False

        return self.orders[order_id]['status']