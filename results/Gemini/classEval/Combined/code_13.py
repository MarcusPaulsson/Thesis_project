class BookManagement:
    """
    Manages a book inventory, allowing adding, removing, and viewing books.
    """

    def __init__(self):
        """
        Initializes an empty book inventory.
        """
        self.inventory = {}

    def add_book(self, title, quantity=1):
        """
        Adds a book to the inventory or increases its quantity if it already exists.

        Args:
            title (str): The title of the book.
            quantity (int, optional): The number of books to add. Defaults to 1.

        Raises:
            TypeError: If title is not a string or quantity is not an integer.
            ValueError: If quantity is not a positive integer.
        """
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        self.inventory[title] = self.inventory.get(title, 0) + quantity

    def remove_book(self, title, quantity):
        """
        Removes a book from the inventory or decreases its quantity.

        Args:
            title (str): The title of the book to remove.
            quantity (int): The number of books to remove.

        Raises:
            TypeError: If title is not a string or quantity is not an integer.
            ValueError: If quantity is not a positive integer.
            Exception: If the book is not in the inventory or there are not enough books to remove.
        """
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        if title not in self.inventory:
            raise Exception("Book not found in inventory.")

        if self.inventory[title] < quantity:
            raise Exception("Not enough books to remove.")

        self.inventory[title] -= quantity
        if self.inventory[title] == 0:
            del self.inventory[title]

    def view_inventory(self):
        """
        Returns the current book inventory.

        Returns:
            dict: A dictionary where keys are book titles and values are their quantities.
        """
        return self.inventory

    def view_book_quantity(self, title):
        """
        Returns the quantity of a specific book in the inventory.

        Args:
            title (str): The title of the book.

        Returns:
            int: The quantity of the book, or 0 if the book is not in the inventory.

        Raises:
            TypeError: If title is not a string.
        """
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")

        return self.inventory.get(title, 0)