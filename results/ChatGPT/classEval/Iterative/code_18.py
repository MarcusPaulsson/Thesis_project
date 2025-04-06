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
        :return: The value corresponding to the key
        """
        converted_key = self._convert_key(key)
        if converted_key not in self._data:
            raise KeyError(f"Key '{converted_key}' not found.")
        return self._data[converted_key]

    def __setitem__(self, key, value):
        """
        Set the value corresponding to the key to the specified value
        :param key: str
        :param value: The specified value
        """
        self._data[self._convert_key(key)] = value

    def __delitem__(self, key):
        """
        Delete the value corresponding to the key
        :param key: str
        """
        converted_key = self._convert_key(key)
        if converted_key not in self._data:
            raise KeyError(f"Key '{converted_key}' not found.")
        del self._data[converted_key]

    def __iter__(self):
        """
        Return an iterator over the keys of the data
        :return: Iterator
        """
        return iter(self._data)

    def __len__(self):
        """
        Return the number of items in the data
        :return: int, length of data
        """
        return len(self._data)

    def _convert_key(self, key):
        """
        Convert key string into camel case
        :param key: str
        :return: converted key string
        """
        return self._to_camel_case(key)

    @staticmethod
    def _to_camel_case(key):
        """
        Convert key string into camel case
        :param key: str
        :return: converted key string
        """
        components = key.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])