class PageUtil:
    """
    PageUtil class is a versatile utility for handling pagination and search functionalities in an efficient and convenient manner.
    """

    def __init__(self, data, page_size):
        """
        Initialize the PageUtil object with the given data and page size.

        :param data: list, the data to be paginated
        :param page_size: int, the number of items per page
        :raises ValueError: if page_size is not a positive integer.
        """
        if not isinstance(page_size, int) or page_size <= 0:
            raise ValueError("Page size must be a positive integer.")

        self.data = data
        self.page_size = page_size
        self.total_items = len(data)
        self.total_pages = (self.total_items + page_size - 1) // page_size

    def get_page(self, page_number):
        """
        Retrieve a specific page of data.

        :param page_number: int, the page number to fetch (1-indexed)
        :return: list, the data on the specified page. Returns an empty list if the page number is invalid.
        """
        if not isinstance(page_number, int) or page_number <= 0 or page_number > self.total_pages:
            return []

        start_index = (page_number - 1) * self.page_size
        end_index = start_index + self.page_size
        return self.data[start_index:end_index]

    def get_page_info(self, page_number):
        """
        Retrieve information about a specific page.

        :param page_number: int, the page number to fetch information about (1-indexed)
        :return: dict, containing page information such as current page number, total pages, etc.
                     Returns an empty dictionary if the page number is invalid.
        """
        if not isinstance(page_number, int) or page_number <= 0 or page_number > self.total_pages:
            return {}

        data = self.get_page(page_number)
        has_previous = page_number > 1
        has_next = page_number < self.total_pages

        page_info = {
            "current_page": page_number,
            "per_page": self.page_size,
            "total_pages": self.total_pages,
            "total_items": self.total_items,
            "has_previous": has_previous,
            "has_next": has_next,
            "data": data
        }
        return page_info

    def search(self, keyword):
        """
        Search for items in the data that contain the given keyword.

        :param keyword: str, the keyword to search for
        :return: dict, containing search information such as total results, total pages, and matching items.
        """
        if not isinstance(keyword, str):
            keyword = str(keyword)

        results = [item for item in self.data if keyword in str(item)]
        total_results = len(results)
        total_pages = (total_results + self.page_size - 1) // self.page_size if total_results > 0 else 0

        search_info = {
            "keyword": keyword,
            "total_results": total_results,
            "total_pages": total_pages,
            "results": results
        }
        return search_info