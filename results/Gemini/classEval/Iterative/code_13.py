class BookManagement:
    """
    Manages a book inventory, allowing adding, removing, viewing, and checking book quantities.
    """

    def __init__(self):
        """
        Initializes the book inventory as an empty dictionary.
        """
        self.inventory = {}

    def add_book(self, title, quantity=1):
        """
        Adds a book to the inventory or increases its quantity if it already exists.

        Args:
            title (str): The title of the book.
            quantity (int, optional): The number of books to add. Defaults to 1.
        Raises:
            TypeError: if title is not a string or quantity is not an integer.
            ValueError: if quantity is not positive.
        """
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        if title in self.inventory:
            self.inventory[title] += quantity
        else:
            self.inventory[title] = quantity

    def remove_book(self, title, quantity):
        """
        Removes a specified quantity of a book from the inventory.

        Args:
            title (str): The title of the book to remove.
            quantity (int): The number of books to remove.

        Returns:
            bool: True if the removal was successful, False otherwise (e.g., book not found or insufficient quantity).
        Raises:
            TypeError: if title is not a string or quantity is not an integer.
            ValueError: if quantity is not positive.
        """
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        if title in self.inventory:
            if self.inventory[title] >= quantity:
                self.inventory[title] -= quantity
                if self.inventory[title] == 0:
                    del self.inventory[title]
                return True
            else:
                return False  # Not enough books to remove
        else:
            return False  # Book not found

    def view_inventory(self):
        """
        Returns the current book inventory.

        Returns:
            dict: A dictionary representing the inventory, where keys are book titles and values are quantities.
        """
        return self.inventory

    def view_book_quantity(self, title):
        """
        Retrieves the quantity of a specific book in the inventory.

        Args:
            title (str): The title of the book to check.

        Returns:
            int: The quantity of the book, or 0 if the book is not found.
        Raises:
            TypeError: if title is not a string.
        """
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        return self.inventory.get(title, 0)