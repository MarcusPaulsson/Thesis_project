class BookManagement:
    """
    This is a class for managing a book system, which supports adding and removing books from the inventory dict,
    viewing the inventory, and checking the quantity of a specific book.
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
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        if title in self.inventory:
            self.inventory[title] += quantity
        else:
            self.inventory[title] = quantity
        
        self.inventory = dict(sorted(self.inventory.items()))

    def remove_book(self, title, quantity):
        """
        Remove one or several books from inventory which is sorted by book title.
        Raise exception when input is invalid.
        :param title: str, the book title
        :param quantity: int
        """
        if title not in self.inventory:
            raise Exception("Book does not exist in inventory.")
        
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        
        if self.inventory[title] < quantity:
            raise Exception("Not enough quantity to remove.")
        
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
        :param title: str, the title of the book.
        :return: int, the quantity of this book title. Returns 0 when the title does not exist in self.inventory
        """
        return self.inventory.get(title, 0)