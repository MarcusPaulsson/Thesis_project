class BookManagement:
    """
    A class to manage a book inventory system, allowing addition, removal, and querying of books.
    """

    def __init__(self):
        """
        Initialize the inventory of the Book Manager.
        """
        self.inventory = {}

    def add_book(self, title: str, quantity: int = 1) -> None:
        """
        Add books to the inventory.
        
        :param title: The title of the book to add
        :param quantity: The number of copies to add, default is 1
        :raises ValueError: If quantity is less than 1
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        self.inventory[title] = self.inventory.get(title, 0) + quantity

    def remove_book(self, title: str, quantity: int) -> None:
        """
        Remove books from the inventory.
        
        :param title: The title of the book to remove
        :param quantity: The number of copies to remove
        :raises ValueError: If quantity is less than 1
        :raises KeyError: If the book is not found in the inventory
        :raises RuntimeError: If there are not enough copies to remove
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        if title not in self.inventory:
            raise KeyError("Book not found in inventory.")
        
        if self.inventory[title] < quantity:
            raise RuntimeError("Not enough copies to remove.")
        
        self.inventory[title] -= quantity
        
        if self.inventory[title] == 0:
            del self.inventory[title]

    def view_inventory(self) -> dict:
        """
        Get the current inventory.
        
        :return: A dictionary of book titles and their quantities
        """
        return self.inventory.copy()

    def view_book_quantity(self, title: str) -> int:
        """
        Get the quantity of a specific book.
        
        :param title: The title of the book
        :return: The quantity of the book, or 0 if it does not exist
        """
        return self.inventory.get(title, 0)