class BookManagement:
    def __init__(self):
        self.inventory = {}


    def add_book(self, title, quantity=1):
        """
        Add one or several books to inventory which is sorted by book title.

        :param title: str, the book title
        :param quantity: int, default value is 1.
        """
        if self.inventory.get(title):
            self.inventory[title] += quantity
        else:
            self.inventory[title] = quantity

    def remove_book(self, title, quantity):
        """
        Remove one or several books from inventory which is sorted by book title.
        Raise false while get invalid input.

        :param title: str, the book title
        :param quantity: int
        """
        if self.inventory.get(title) and quantity <= self.inventory[title]:
            self.inventory[title] -= quantity
        else:
            raise ValueError("Cannot remove more books than in inventory")

    def view_inventory(self):
        """
        Get the inventory of the Book Management.

        :return self.inventory: dictionary, {title(str): quantity(int), ...}
        """
        return self.inventory

    def view_book_quantity(self, title):
        """
        Get the quantity of a book.

        :param title: str, the title of the book.
        :return quantity: the quantity of this book title. return 0 when the title does not exist in self.inventory
        """
        return self.inventory.get(title, 0)