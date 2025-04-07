class Warehouse:
    """
    The class manages inventory and orders, including adding products, updating product quantities, retrieving product quantities, creating orders, changing order statuses, and tracking orders.
    """

    def __init__(self):
        """
        Initialize two fields.
        self.inventory is a dict that stores the products.
        self.inventory = {Product ID: Product}
        self.orders is a dict that stores the products in an order.
        self.orders = {Order ID: Order}
        """
        self.inventory = {}  # Product ID: Product
        self.orders = {}  # Order ID: Order

    def add_product(self, product_id, name, quantity):
        """
        Add product to inventory, increasing the quantity if it already exists.
        :param product_id: int
        :param name: str, product name
        :param quantity: int, product quantity
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity
        else:
            self.inventory[product_id] = {'name': name, 'quantity': quantity}

    def update_product_quantity(self, product_id, quantity):
        """
        Update the quantity of a product in inventory.
        :param product_id: int
        :param quantity: int, amount to add (can be negative)
        """
        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity
            if self.inventory[product_id]['quantity'] <= 0:
                del self.inventory[product_id]
        else:
            raise KeyError("Product ID not found in inventory.")

    def get_product_quantity(self, product_id):
        """
        Get the quantity of a specific product by product_id.
        :param product_id: int
        :return: int or False
        """
        return self.inventory[product_id]['quantity'] if product_id in self.inventory else False

    def create_order(self, order_id, product_id, quantity):
        """
        Create an order which includes the information of product, like id and quantity.
        The default value of status is 'Shipped'.
        :param order_id: int
        :param product_id: int
        :param quantity: int, the quantity of product that is selected.
        :return: False if product_id is not in inventory or the quantity is not adequate.
        """
        if product_id in self.inventory and self.inventory[product_id]['quantity'] >= quantity:
            self.orders[order_id] = {'product_id': product_id, 'quantity': quantity, 'status': 'Shipped'}
            self.update_product_quantity(product_id, -quantity)
        else:
            return False

    def change_order_status(self, order_id, status):
        """
        Change the status of an order if the input order_id is in self.orders.
        :param order_id: int
        :param status: str, the state that is going to change to
        :return: False if the order_id is not in self.orders.
        """
        if order_id in self.orders:
            self.orders[order_id]['status'] = status
        else:
            return False

    def track_order(self, order_id):
        """
        Get the status of a specific order.
        :param order_id: int
        :return: str or False
        """
        return self.orders[order_id]['status'] if order_id in self.orders else False