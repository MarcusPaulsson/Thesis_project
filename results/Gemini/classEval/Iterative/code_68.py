class PageUtil:
    """
    PageUtil class is a utility for handling pagination and search functionalities.
    """

    def __init__(self, data, page_size):
        """
        Initialize the PageUtil object.

        :param data: list, the data to be paginated
        :param page_size: int, the number of items per page
        :raises TypeError: if data is not a list or page_size is not an integer.
        :raises ValueError: if page_size is not a positive integer.
        """
        if not isinstance(data, list):
            raise TypeError("Data must be a list.")
        if not isinstance(page_size, int):
            raise TypeError("Page size must be an integer.")
        if page_size <= 0:
            raise ValueError("Page size must be a positive integer.")

        self.data = data
        self.page_size = page_size
        self.total_items = len(data)
        self.total_pages = (self.total_items + page_size - 1) // page_size

    def get_page(self, page_number):
        """
        Retrieve a specific page of data.

        :param page_number: int, the page number to fetch (1-indexed)
        :return: list, the data on the specified page
        :raises TypeError: if page_number is not an integer.
        :raises ValueError: if page_number is not a positive integer or exceeds total pages.
        """
        if not isinstance(page_number, int):
            raise TypeError("Page number must be an integer.")
        if page_number <= 0:
            raise ValueError("Page number must be a positive integer.")
        if page_number > self.total_pages and self.total_pages > 0:
            raise ValueError("Page number exceeds total pages.")

        start_index = (page_number - 1) * self.page_size
        end_index = min(start_index + self.page_size, self.total_items)
        return self.data[start_index:end_index]

    def get_page_info(self, page_number):
        """
        Retrieve information about a specific page.

        :param page_number: int, the page number to fetch information about (1-indexed)
        :return: dict, containing page information.
        :raises TypeError: if page_number is not an integer.
        :raises ValueError: if page_number is not a positive integer or exceeds total pages.
        """
        if not isinstance(page_number, int):
            raise TypeError("Page number must be an integer.")
        if page_number <= 0:
            raise ValueError("Page number must be a positive integer.")
        if page_number > self.total_pages and self.total_pages > 0:
            raise ValueError("Page number exceeds total pages.")

        start_index = (page_number - 1) * self.page_size
        end_index = min(start_index + self.page_size, self.total_items)
        data = self.data[start_index:end_index]
        has_previous = page_number > 1
        has_next = page_number < self.total_pages

        return {
            "current_page": page_number,
            "per_page": self.page_size,
            "total_pages": self.total_pages,
            "total_items": self.total_items,
            "has_previous": has_previous,
            "has_next": has_next,
            "data": data
        }

    def search(self, keyword):
        """
        Search for items in the data that contain the given keyword (case-insensitive).

        :param keyword: str, the keyword to search for
        :return: dict, containing search information.
        :raises TypeError: if keyword is not a string.
        """
        if not isinstance(keyword, str):
            raise TypeError("Keyword must be a string.")

        results = [item for item in self.data if keyword.lower() in str(item).lower()]
        total_results = len(results)
        total_pages = (total_results + self.page_size - 1) // self.page_size if self.page_size > 0 else 0

        search_info = {
            "keyword": keyword,
            "total_results": total_results,
            "total_pages": total_pages,
            "results": results
        }
        return search_info