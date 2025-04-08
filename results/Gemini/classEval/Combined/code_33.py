class DiscountStrategy:
    """
    This class implements different discount strategies for a shopping cart.
    """

    def __init__(self, customer, cart, promotion=None):
        """
        Initializes the DiscountStrategy.

        :param customer: dict, customer information (e.g., {'fidelity': 1200})
        :param cart: list of dicts, items in the cart (e.g., [{'product': 'A', 'quantity': 2, 'price': 10}])
        :param promotion: function, optional promotion to apply
        """
        self.customer = customer
        self.cart = cart
        self.promotion = promotion
        self._total = self._calculate_total()

    def _calculate_total(self):
        """
        Calculates the total cost of the items in the cart.

        :return: float, the total cost
        """
        return sum(item['quantity'] * item['price'] for item in self.cart)

    def total(self):
        """
        Returns the total cost of items in the cart.

        :return: float, the total cost
        """
        return self._total

    def due(self):
        """
        Calculates the final amount due after applying any discounts.

        :return: float, the final amount due
        """
        discount = 0
        if self.promotion:
            discount = self.promotion(self)
        return self.total() - discount

    @staticmethod
    def FidelityPromo(order):
        """
        Applies a 5% discount if the customer has 1000 or more fidelity points.

        :param order: DiscountStrategy, the order object
        :return: float, the discount amount
        """
        if order.customer.get('fidelity', 0) >= 1000:
            return order.total() * 0.05
        return 0.0

    @staticmethod
    def BulkItemPromo(order):
        """
        Applies a 10% discount on items where the quantity is 20 or more.

        :param order: DiscountStrategy, the order object
        :return: float, the discount amount
        """
        discount = 0
        for item in order.cart:
            if item['quantity'] >= 20:
                discount += item['quantity'] * item['price'] * 0.1
        return discount

    @staticmethod
    def LargeOrderPromo(order):
        """
        Applies a 7% discount if there are 10 or more different products in the cart.

        :param order: DiscountStrategy, the order object
        :return: float, the discount amount
        """
        if len(order.cart) >= 10:
            return order.total() * 0.07
        return 0.0