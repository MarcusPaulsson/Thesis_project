class DiscountStrategy:
    """
    This is a class that allows to use different discount strategy based on shopping credit or shopping cart in supermarket.
    """

    def __init__(self, customer, cart, promotion=None):
        """
        Initialize the DiscountStrategy with customer information, a cart of items, and an optional promotion.
        :param customer: dict, customer information
        :param cart: list of dicts, a cart of items with details
        :param promotion: function, optional promotion applied to the order
        """
        self.customer = customer
        self.cart = cart
        self.promotion = promotion
        self._total = self._calculate_total()

    def _calculate_total(self):
        """
        Calculate the total cost of items in the cart.
        :return: float, total cost of items
        """
        total = 0.0
        for item in self.cart:
            total += item['quantity'] * item['price']
        return total

    def total(self):
        """
        Return the total cost of items in the cart.
        :return: float, total cost of items
        """
        return self._total

    def due(self):
        """
        Calculate the final amount to be paid after applying the discount.
        :return: float, final amount to be paid
        """
        if self.promotion:
            discount = self.promotion(self)
        else:
            discount = 0.0
        return self._total - discount

    @staticmethod
    def FidelityPromo(order):
        """
        Calculate the discount based on the fidelity points of the customer.
        Customers with over 1000 points can enjoy a 5% discount on the entire order.
        :param order: DiscountStrategy, the order to apply the discount to
        :return: float, discount amount
        """
        if order.customer.get('fidelity', 0) >= 1000:
            return order.total() * 0.05
        return 0.0

    @staticmethod
    def BulkItemPromo(order):
        """
        Calculate the discount based on bulk item quantity in the order.
        In the same order, if the quantity of a single item reaches 20 or more, each item will enjoy a 10% discount.
        :param order: DiscountStrategy, the order to apply the discount to
        :return: float, discount amount
        """
        discount = 0.0
        for item in order.cart:
            if item['quantity'] >= 20:
                discount += item['quantity'] * item['price'] * 0.10
        return discount

    @staticmethod
    def LargeOrderPromo(order):
        """
        Calculate the discount based on the number of different products in the order.
        If the quantity of different products in the order reaches 10 or more, the entire order will enjoy a 7% discount.
        :param order: DiscountStrategy, the order to apply the discount to
        :return: float, discount amount
        """
        if len(order.cart) >= 10:
            return order.total() * 0.07
        return 0.0


if __name__ == '__main__':
    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
    ds_fidelity = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
    print(f"Total with FidelityPromo: {ds_fidelity.due()}")  # Output: 312.55

    ds_no_promo = DiscountStrategy(customer, cart)
    print(f"Total without promo: {ds_no_promo.total()}")  # Output: 329.0

    cart_bulk = [{'product': 'product', 'quantity': 20, 'price': 23.5}]
    ds_bulk = DiscountStrategy(customer, cart_bulk, DiscountStrategy.BulkItemPromo)
    print(f"Total with BulkItemPromo: {ds_bulk.due()}")  # Output: 423.0

    cart_large = [{'product': 'product1', 'quantity': 1, 'price': 23.5},
                  {'product': 'product2', 'quantity': 1, 'price': 23.5},
                  {'product': 'product3', 'quantity': 1, 'price': 23.5},
                  {'product': 'product4', 'quantity': 1, 'price': 23.5},
                  {'product': 'product5', 'quantity': 1, 'price': 23.5},
                  {'product': 'product6', 'quantity': 1, 'price': 23.5},
                  {'product': 'product7', 'quantity': 1, 'price': 23.5},
                  {'product': 'product8', 'quantity': 1, 'price': 23.5},
                  {'product': 'product9', 'quantity': 1, 'price': 23.5},
                  {'product': 'product10', 'quantity': 1, 'price': 23.5}]
    ds_large = DiscountStrategy(customer, cart_large, DiscountStrategy.LargeOrderPromo)
    print(f"Total with LargeOrderPromo: {ds_large.due()}")  # Output: 217.15000000000003