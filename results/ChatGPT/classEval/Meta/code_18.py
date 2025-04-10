class CamelCaseMap:
    """
    This is a custom class that allows keys to be in camel case style by converting them from underscore style, which provides dictionary-like functionality.
    """

    def __init__(self):
        """
        Initialize data to an empty dictionary
        """
        self._data = {}

    def __getitem__(self, key):
        """
        Return the value corresponding to the key
        :param key: str
        :return: str, the value corresponding to the key
        """
        key = self._convert_key(key)
        return self._data[key]

    def __setitem__(self, key, value):
        """
        Set the value corresponding to the key to the specified value
        :param key: str
        :param value: str, the specified value
        :return: None
        """
        key = self._convert_key(key)
        self._data[key] = value

    def __delitem__(self, key):
        """
        Delete the value corresponding to the key
        :param key: str
        :return: None
        """
        key = self._convert_key(key)
        del self._data[key]

    def __iter__(self):
        """
        Returning Iterable Objects with Own Data
        :return: Iterator
        """
        return iter(self._data.keys())

    def __len__(self):
        """
        Returns the length of the own data
        :return: int, length of data
        """
        return len(self._data)

    def _convert_key(self, key):
        """
        Convert key string into camel case
        :param key: str
        :return: str, converted key string
        """
        if not isinstance(key, str):
            return key
        return self._to_camel_case(key)

    @staticmethod
    def _to_camel_case(key):
        """
        Convert key string into camel case
        :param key: str
        :return: str, converted key string
        """
        if not isinstance(key, str):
            return key
        parts = key.split('_')
        return parts[0] + ''.join(part.capitalize() for part in parts[1:])