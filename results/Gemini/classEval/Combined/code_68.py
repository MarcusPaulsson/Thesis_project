class PageUtil:
    """
    Utility class for handling pagination and search functionalities.
    """

    def __init__(self, data, page_size):
        """
        Initializes the PageUtil object.

        Args:
            data (list): The data to be paginated.
            page_size (int): The number of items per page.
        """
        if not isinstance(data, list):
            raise TypeError("Data must be a list.")
        if not isinstance(page_size, int) or page_size <= 0:
            raise ValueError("Page size must be a positive integer.")

        self.data = data
        self.page_size = page_size
        self.total_items = len(data)
        self.total_pages = (self.total_items + page_size - 1) // page_size

    def get_page(self, page_number):
        """
        Retrieves a specific page of data.

        Args:
            page_number (int): The page number to fetch (1-indexed).

        Returns:
            list: The data on the specified page, or an empty list if the page number is invalid.
        """
        if not isinstance(page_number, int):
            raise TypeError("Page number must be an integer.")

        if page_number <= 0 or page_number > self.total_pages:
            return []

        start_index = (page_number - 1) * self.page_size
        end_index = min(start_index + self.page_size, self.total_items)
        return self.data[start_index:end_index]

    def get_page_info(self, page_number):
        """
        Retrieves information about a specific page.

        Args:
            page_number (int): The page number to fetch information about (1-indexed).

        Returns:
            dict: A dictionary containing page information, or an empty dictionary if the page number is invalid.
        """
        if not isinstance(page_number, int):
            raise TypeError("Page number must be an integer.")

        if page_number <= 0 or page_number > self.total_pages:
            return {}

        page_data = self.get_page(page_number)
        has_previous = page_number > 1
        has_next = page_number < self.total_pages

        page_info = {
            "current_page": page_number,
            "per_page": self.page_size,
            "total_pages": self.total_pages,
            "total_items": self.total_items,
            "has_previous": has_previous,
            "has_next": has_next,
            "data": page_data,
        }
        return page_info

    def search(self, keyword):
        """
        Searches for items in the data that contain the given keyword (case-insensitive).

        Args:
            keyword (str): The keyword to search for.

        Returns:
            dict: A dictionary containing search information.
        """
        if not isinstance(keyword, str):
            raise TypeError("Keyword must be a string.")

        keyword = str(keyword).lower()  # Convert keyword to string and lowercase
        results = [item for item in self.data if keyword in str(item).lower()]  # Case-insensitive search
        total_results = len(results)
        total_pages = (total_results + self.page_size - 1) // self.page_size if total_results > 0 else 0

        search_info = {
            "keyword": keyword,
            "total_results": total_results,
            "total_pages": total_pages,
            "results": results,
        }
        return search_info