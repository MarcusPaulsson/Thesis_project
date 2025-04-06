class Warehouse:
    """
    The class manages inventory and orders, including adding products, updating product quantities,
    retrieving product quantities, creating orders, changing order statuses, and tracking orders.
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
        Add product to inventory or update the quantity if it already exists.
        :param product_id: int
        :param name: str, product name
        :param quantity: int, product quantity
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity
        else:
            self.inventory[product_id] = {'name': name, 'quantity': quantity}

    def update_product_quantity(self, product_id, quantity):
        """
        Update the quantity of a product in inventory based on product_id.
        :param product_id: int
        :param quantity: int, quantity to add (can be negative to remove)
        """
        if product_id not in self.inventory:
            raise ValueError("Product ID does not exist in inventory.")
        
        if self.inventory[product_id]['quantity'] + quantity < 0:
            raise ValueError("Insufficient quantity in inventory.")
        
        self.inventory[product_id]['quantity'] += quantity

    def get_product_quantity(self, product_id):
        """
        Get the quantity of a specific product by product_id.
        :param product_id: int
        :return: int quantity of product or None if not found
        """
        return self.inventory.get(product_id, {}).get('quantity')

    def create_order(self, order_id, product_id, quantity):
        """
        Create an order which includes the information of product, like id and quantity.
        :param order_id: int
        :param product_id: int
        :param quantity: int, quantity of product to order
        :return: bool indicating success of order creation
        """
        if product_id not in self.inventory or self.inventory[product_id]['quantity'] < quantity:
            return False
        
        self.orders[order_id] = {
            'product_id': product_id,
            'quantity': quantity,
            'status': 'Shipped'
        }
        self.update_product_quantity(product_id, -quantity)
        return True

    def change_order_status(self, order_id, status):
        """
        Change the status of an order if the input order_id is in self.orders.
        :param order_id: int
        :param status: str, the state to change to
        :return: bool indicating success of status change
        """
        if order_id in self.orders:
            self.orders[order_id]['status'] = status
            return True
        return False

    def track_order(self, order_id):
        """
        Get the status of a specific order.
        :param order_id: int
        :return: str status of the order or None if not found
        """
        return self.orders.get(order_id, {}).get('status')