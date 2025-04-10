class BookManagement:
    """
    A class that manages a simple book inventory system, allowing for adding and removing books,
    viewing the inventory, and checking the quantity of specific titles.
    """

    def __init__(self):
        """Initialize the inventory for the Book Management system."""
        self.inventory = {}

    def add_book(self, title: str, quantity: int = 1):
        """
        Add books to the inventory.

        :param title: str, the title of the book.
        :param quantity: int, the number of copies to add (default is 1).
        :raises ValueError: if quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        self.inventory[title] = self.inventory.get(title, 0) + quantity

    def remove_book(self, title: str, quantity: int):
        """
        Remove books from the inventory.

        :param title: str, the title of the book.
        :param quantity: int, the number of copies to remove.
        :raises ValueError: if quantity is less than 1.
        :raises KeyError: if the book does not exist in the inventory.
        :raises ValueError: if there are not enough copies to remove.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        if title not in self.inventory:
            raise KeyError("Book does not exist in inventory.")
        
        if self.inventory[title] < quantity:
            raise ValueError("Not enough copies to remove.")
        
        self.inventory[title] -= quantity
        
        if self.inventory[title] == 0:
            del self.inventory[title]

    def view_inventory(self) -> dict:
        """
        Get the current inventory.

        :return: dict, a dictionary of books and their quantities.
        """
        return self.inventory.copy()

    def view_book_quantity(self, title: str) -> int:
        """
        Get the quantity of a specific book.

        :param title: str, the title of the book.
        :return: int, the quantity of the book or 0 if not found.
        """
        return self.inventory.get(title, 0)