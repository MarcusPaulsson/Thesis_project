class PageUtil:
    """
    PageUtil class is a versatile utility for handling pagination and search functionalities in an efficient and convenient manner.
    """

    def __init__(self, data, page_size):
        """
        Initialize the PageUtil object with the given data and page size.
        :param data: list, the data to be paginated
        :param page_size: int, the number of items per page
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
        Retrieve a specific page of data.
        :param page_number: int, the page number to fetch
        :return: list, the data on the specified page
        """
        if not isinstance(page_number, int) or page_number <= 0:
            raise ValueError("Page number must be a positive integer.")
        if page_number > self.total_pages:
            return []

        start_index = (page_number - 1) * self.page_size
        end_index = start_index + self.page_size
        return self.data[start_index:end_index]

    def get_page_info(self, page_number):
        """
        Retrieve information about a specific page.
        :param page_number: int, the page number to fetch information about
        :return: dict, containing page information such as current page number, total pages, etc.
        """
        if not isinstance(page_number, int) or page_number <= 0:
            raise ValueError("Page number must be a positive integer.")

        if page_number > self.total_pages:
             return {
                "current_page": page_number,
                "per_page": self.page_size,
                "total_pages": self.total_pages,
                "total_items": self.total_items,
                "has_previous": page_number > 1,
                "has_next": False,  # No next page if page_number exceeds total_pages
                "data": []
            }

        page_data = self.get_page(page_number)
        has_previous = page_number > 1
        has_next = page_number < self.total_pages

        return {
            "current_page": page_number,
            "per_page": self.page_size,
            "total_pages": self.total_pages,
            "total_items": self.total_items,
            "has_previous": has_previous,
            "has_next": has_next,
            "data": page_data
        }

    def search(self, keyword):
        """
        Search for items in the data that contain the given keyword.
        :param keyword: str, the keyword to search for
        :return: dict, containing search information such as total results and matching items
        """
        if not isinstance(keyword, str):
            raise TypeError("Keyword must be a string.")

        results = [item for item in self.data if str(item).find(keyword) != -1]
        total_results = len(results)
        total_pages = (total_results + self.page_size - 1) // self.page_size

        search_info = {
            "keyword": keyword,
            "total_results": total_results,
            "total_pages": total_pages,
            "results": results
        }
        return search_info