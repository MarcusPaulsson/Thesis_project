class DiscountStrategy:
    """
    This class allows the use of different discount strategies based on shopping credit or shopping cart in a supermarket.
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

    def total(self):
        """
        Calculate the total cost of items in the cart.
        :return: float, total cost of items
        """
        return sum(item['quantity'] * item['price'] for item in self.cart)

    def due(self):
        """
        Calculate the final amount to be paid after applying the discount.
        :return: float, final amount to be paid
        """
        total_cost = self.total()
        discount = self.promotion(self) if self.promotion else 0
        return total_cost - discount

    @staticmethod
    def FidelityPromo(order):
        """
        Calculate the discount based on the fidelity points of the customer.
        :param order: DiscountStrategy, the order to apply the discount to
        :return: float, discount amount
        """
        if order.customer['fidelity'] >= 1000:
            return order.total() * 0.05
        return 0.0

    @staticmethod
    def BulkItemPromo(order):
        """
        Calculate the discount based on bulk item quantity in the order.
        :param order: DiscountStrategy, the order to apply the discount to
        :return: float, discount amount
        """
        discount = sum(item['quantity'] * item['price'] * 0.10 
                       for item in order.cart if item['quantity'] >= 20)
        return discount

    @staticmethod
    def LargeOrderPromo(order):
        """
        Calculate the discount based on the number of different products in the order.
        :param order: DiscountStrategy, the order to apply the discount to
        :return: float, discount amount
        """
        if len(order.cart) >= 10:
            return order.total() * 0.07
        return 0.0