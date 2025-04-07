class Warehouse:
    def __init__(self):
        self.inventory = {}  # Product ID: Product
        self.orders = {}  # Order ID: Order

    def add_product(self, product_id, name, quantity):
        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity
        else:
            self.inventory[product_id] = {'name': name, 'quantity': quantity}

    def update_product_quantity(self, product_id, quantity):
        if product_id in self.inventory:
            new_quantity = self.inventory[product_id]['quantity'] + quantity
            if new_quantity < 0:
                new_quantity = 0
            self.inventory[product_id]['quantity'] = new_quantity
            if new_quantity == 0:
                del self.inventory[product_id]

    def get_product_quantity(self, product_id):
        if product_id in self.inventory:
            return self.inventory[product_id]['quantity']
        return False

    def create_order(self, order_id, product_id, quantity):
        if product_id not in self.inventory or self.inventory[product_id]['quantity'] < quantity:
            return False
        self.orders[order_id] = {'product_id': product_id, 'quantity': quantity, 'status': 'Shipped'}
        self.update_product_quantity(product_id, -quantity)

    def change_order_status(self, order_id, status):
        if order_id in self.orders:
            self.orders[order_id]['status'] = status
        else:
            return False

    def track_order(self, order_id):
        if order_id in self.orders:
            return self.orders[order_id]['status']
        return False