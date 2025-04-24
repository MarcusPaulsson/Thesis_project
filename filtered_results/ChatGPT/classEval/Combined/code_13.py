class BookManagement:
    """
    A class to manage a book inventory system, supporting adding and removing books,
    viewing the inventory, and checking the quantity of specific books.
    """

    def __init__(self):
        """
        Initialize the inventory of the Book Manager.
        """
        self.inventory = {}

    def add_book(self, title: str, quantity: int = 1) -> None:
        """
        Add one or several books to the inventory.
        
        :param title: str, the book title
        :param quantity: int, the number of books to add (default is 1)
        :raises ValueError: if quantity is less than 1
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        self.inventory[title] = self.inventory.get(title, 0) + quantity

    def remove_book(self, title: str, quantity: int) -> None:
        """
        Remove one or several books from the inventory.
        
        :param title: str, the book title
        :param quantity: int, the number of books to remove
        :raises ValueError: if the book is not found or if the quantity is invalid
        """
        if title not in self.inventory:
            raise ValueError("Book not found in inventory.")
        
        if quantity < 1 or quantity > self.inventory[title]:
            raise ValueError("Invalid quantity for removal.")
        
        self.inventory[title] -= quantity
        
        if self.inventory[title] == 0:
            del self.inventory[title]

    def view_inventory(self) -> dict:
        """
        Get the current inventory of the Book Management.
        
        :return: dict, {title(str): quantity(int), ...}
        """
        return self.inventory

    def view_book_quantity(self, title: str) -> int:
        """
        Get the quantity of a specific book.
        
        :param title: str, the title of the book
        :return: int, the quantity of the book; returns 0 if the title does not exist
        """
        return self.inventory.get(title, 0)