class BookManagement:
    """
    This is a class for managing a book system, which supports adding and removing books from the inventory,
    viewing the inventory, and checking the quantity of a specific book.
    """

    def __init__(self):
        """
        Initialize the inventory of the Book Manager.
        """
        self.inventory = {}

    def add_book(self, title, quantity=1):
        """
        Add one or several books to the inventory sorted by book title.
        :param title: str, the book title
        :param quantity: int, default value is 1
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        if title in self.inventory:
            self.inventory[title] += quantity
        else:
            self.inventory[title] = quantity
        
        self.inventory = dict(sorted(self.inventory.items()))

    def remove_book(self, title, quantity):
        """
        Remove one or several books from inventory sorted by book title.
        Raise ValueError for invalid input.
        :param title: str, the book title
        :param quantity: int
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        if title not in self.inventory:
            raise ValueError("Book not found in inventory.")
        
        if quantity > self.inventory[title]:
            raise ValueError("Insufficient quantity to remove.")
        
        self.inventory[title] -= quantity
        
        if self.inventory[title] == 0:
            del self.inventory[title]

    def view_inventory(self):
        """
        Get the inventory of the Book Management.
        :return: dictionary, {title(str): quantity(int), ...}
        """
        return self.inventory

    def view_book_quantity(self, title):
        """
        Get the quantity of a book.
        :param title: str, the title of the book
        :return: int, the quantity of this book title, returns 0 when the title does not exist in inventory
        """
        return self.inventory.get(title, 0)