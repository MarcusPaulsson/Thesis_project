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
        self._total = self.calculate_total()

    def calculate_total(self):
        """
        Calculate the total cost of items in the cart.
        :return: float, total cost of items
        """
        total = sum(item['quantity'] * item['price'] for item in self.cart)
        return total

    def due(self):
        """
        Calculate the final amount to be paid after applying the discount.
        :return: float, final amount to be paid
        """
        discount = 0
        if self.promotion:
            discount = self.promotion(self)
        return self._total - discount

    @staticmethod
    def fidelity_promo(order):
        """
        Calculate the discount based on the fidelity points of the customer.
        Customers with over 1000 points can enjoy a 5% discount on the entire order.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        """
        if order.customer.get('fidelity', 0) >= 1000:
            return order._total * 0.05
        return 0.0

    @staticmethod
    def bulk_item_promo(order):
        """
        Calculate the discount based on bulk item quantity in the order.
        In the same order, if the quantity of a single item reaches 20 or more, each item will enjoy a 10% discount.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        """
        discount = 0
        for item in order.cart:
            if item['quantity'] >= 20:
                discount += item['quantity'] * item['price'] * 0.1
        return discount

    @staticmethod
    def large_order_promo(order):
        """
        Calculate the discount based on the number of different products in the order.
        If the quantity of different products in the order reaches 10 or more, the entire order will enjoy a 7% discount.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        """
        if len(order.cart) >= 10:
            return order._total * 0.07
        return 0.0


if __name__ == '__main__':
    # Example Usage
    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': 'product1', 'quantity': 14, 'price': 23.5},
            {'product': 'product2', 'quantity': 25, 'price': 10.0}]

    # Fidelity Promo
    order1 = DiscountStrategy(customer, cart, DiscountStrategy.fidelity_promo)
    print(f"Total with Fidelity Promo: {order1.due()}")

    # Bulk Item Promo
    order2 = DiscountStrategy(customer, cart, DiscountStrategy.bulk_item_promo)
    print(f"Total with Bulk Item Promo: {order2.due()}")

    # Large Order Promo
    cart_large = [{'product': f'product{i}', 'quantity': 1, 'price': 5} for i in range(10)}]
    order3 = DiscountStrategy(customer, cart_large, DiscountStrategy.large_order_promo)
    print(f"Total with Large Order Promo: {order3.due()}")

    # No Promo
    order4 = DiscountStrategy(customer, cart)
    print(f"Total with No Promo: {order4.due()}")