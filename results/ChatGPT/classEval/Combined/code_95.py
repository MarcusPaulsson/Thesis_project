class Warehouse:
    """
    The class manages inventory and orders, including adding products, updating product quantities,
    retrieving product quantities, creating orders, changing order statuses, and tracking orders.
    """

    def __init__(self):
        """Initialize inventory and orders as empty dictionaries."""
        self.inventory = {}  # Product ID: Product
        self.orders = {}  # Order ID: Order

    def add_product(self, product_id: int, name: str, quantity: int) -> None:
        """
        Add a product to the inventory or increase its quantity if it already exists.
        :param product_id: int
        :param name: str, product name
        :param quantity: int, product quantity
        """
        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity
        else:
            self.inventory[product_id] = {'name': name, 'quantity': quantity}

    def update_product_quantity(self, product_id: int, quantity: int) -> None:
        """
        Update the quantity of a product in inventory.
        :param product_id: int
        :param quantity: int, the quantity to add (can be negative)
        """
        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity
            if self.inventory[product_id]['quantity'] <= 0:
                del self.inventory[product_id]

    def get_product_quantity(self, product_id: int) -> int or bool:
        """
        Get the quantity of a specific product by product_id.
        :param product_id: int
        :return: the quantity if the product_id is in inventory, otherwise False.
        """
        return self.inventory.get(product_id, {}).get('quantity', False)

    def create_order(self, order_id: int, product_id: int, quantity: int) -> bool:
        """
        Create an order for a product if available in sufficient quantity.
        :param order_id: int
        :param product_id: int
        :param quantity: int, the quantity of product selected.
        :return: False if product_id is not in inventory or quantity is not adequate, otherwise None.
        """
        if product_id not in self.inventory or self.inventory[product_id]['quantity'] < quantity:
            return False

        self.orders[order_id] = {
            'product_id': product_id,
            'quantity': quantity,
            'status': 'Shipped'
        }
        self.update_product_quantity(product_id, -quantity)

    def change_order_status(self, order_id: int, status: str) -> bool:
        """
        Change the status of an order if the order_id exists.
        :param order_id: int
        :param status: str, the new status to set
        :return: False if the order_id is not in self.orders, otherwise None.
        """
        if order_id in self.orders:
            self.orders[order_id]['status'] = status
            return True
        return False

    def track_order(self, order_id: int) -> str or bool:
        """
        Get the status of a specific order.
        :param order_id: int
        :return: the status if order_id is in self.orders, otherwise False.
        """
        return self.orders.get(order_id, {}).get('status', False)