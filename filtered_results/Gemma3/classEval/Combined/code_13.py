class BookManagement:
    """
    This is a class for managing books, supporting adding, removing, viewing inventory,
    and checking the quantity of a specific book.
    """

    def __init__(self):
        """
        Initializes the book inventory as an empty dictionary.
        """
        self.inventory = {}

    def add_book(self, title, quantity=1):
        """
        Adds a book to the inventory or increases its quantity if it already exists.

        :param title: The title of the book (string).
        :param quantity: The quantity to add (integer, default is 1).
        """
        if title in self.inventory:
            self.inventory[title] += quantity
        else:
            self.inventory[title] = quantity

    def remove_book(self, title, quantity):
        """
        Removes books from the inventory.

        :param title: The title of the book to remove (string).
        :param quantity: The quantity to remove (integer).
        :raises Exception: If the book is not found, the quantity is invalid,
                          or the quantity to remove exceeds the available quantity.
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
        Returns the current inventory.

        :return: A dictionary representing the inventory, where keys are book titles
                 and values are their quantities.
        """
        return self.inventory

    def view_book_quantity(self, title):
        """
        Returns the quantity of a specific book in the inventory.

        :param title: The title of the book (string).
        :return: The quantity of the book (integer). Returns 0 if the book is not found.
        """
        return self.inventory.get(title, 0)