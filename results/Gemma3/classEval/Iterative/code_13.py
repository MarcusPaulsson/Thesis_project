class BookManagement:
    """
    This is a class as managing books system, which supports to add and remove books from the inventory dict, view the inventory, and check the quantity of a specific book.
    """

    def __init__(self):
        """
        Initialize the inventory of Book Manager.
        """
        self.inventory = {}

    def add_book(self, title, quantity=1):
        """
        Add one or several books to inventory which is sorted by book title.
        :param title: str, the book title
        :param quantity: int, default value is 1.
        """
        if title in self.inventory:
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
        if title not in self.inventory:
            raise Exception("Book not found in inventory.")
        if quantity <= 0:
            raise Exception("Quantity must be positive.")
        if quantity > self.inventory[title]:
            raise Exception("Quantity to remove exceeds available quantity.")

        self.inventory[title] -= quantity
        if self.inventory[title] == 0:
            del self.inventory[title]

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
        :return quantity: the quantity of this book title. return 0 when the title does not exist in self.invenroty
        """
        if title in self.inventory:
            return self.inventory[title]
        else:
            return 0