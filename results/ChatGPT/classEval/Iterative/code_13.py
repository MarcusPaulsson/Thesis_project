class BookManagement:
    """
    A class to manage a book inventory system, allowing for the addition and removal of books,
    viewing the inventory, and checking the quantity of a specific book.
    """

    def __init__(self):
        """
        Initialize the inventory of the Book Manager.
        """
        self.inventory = {}

    def add_book(self, title: str, quantity: int = 1):
        """
        Add one or several copies of a book to the inventory, sorted by book title.
        
        :param title: str, the book title
        :param quantity: int, default value is 1 (must be a positive integer)
        :raises ValueError: if title is not a string or quantity is not a positive integer
        """
        if not isinstance(title, str) or not isinstance(quantity, int) or quantity < 1:
            raise ValueError("Invalid input: title must be a string and quantity must be a positive integer.")
        
        self.inventory[title] = self.inventory.get(title, 0) + quantity
        self.inventory = dict(sorted(self.inventory.items()))

    def remove_book(self, title: str, quantity: int):
        """
        Remove one or several copies of a book from the inventory, sorted by book title.
        
        :param title: str, the book title
        :param quantity: int, the number of copies to remove
        :raises ValueError: if title is not found or if there are not enough books to remove
        """
        if not isinstance(title, str) or not isinstance(quantity, int) or quantity < 1:
            raise ValueError("Invalid input: title must be a string and quantity must be a positive integer.")
        
        if title not in self.inventory:
            raise ValueError("Book not found in inventory.")

        if self.inventory[title] < quantity:
            raise ValueError("Not enough books to remove.")

        self.inventory[title] -= quantity

        if self.inventory[title] == 0:
            del self.inventory[title]

        self.inventory = dict(sorted(self.inventory.items()))

    def view_inventory(self) -> dict:
        """
        Get the inventory of the Book Management.
        
        :return: dictionary, {title(str): quantity(int), ...}
        """
        return self.inventory

    def view_book_quantity(self, title: str) -> int:
        """
        Get the quantity of a specific book in the inventory.
        
        :param title: str, the title of the book
        :return: int, the quantity of the specified book title (returns 0 if not found)
        """
        return self.inventory.get(title, 0)