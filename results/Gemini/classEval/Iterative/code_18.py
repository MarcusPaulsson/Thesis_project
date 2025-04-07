class CamelCaseMap:
    """
    A dictionary-like class that automatically converts keys from underscore_case to camelCase.
    """

    def __init__(self):
        """
        Initializes an empty dictionary to store the data.
        """
        self._data = {}

    def __getitem__(self, key):
        """
        Retrieves the value associated with the given key (underscore_case).

        Args:
            key (str): The key to look up (in underscore_case).

        Returns:
            The value associated with the camelCase version of the key.

        Raises:
            KeyError: If the camelCase key is not found.
        """
        camel_case_key = self._convert_key(key)
        return self._data[camel_case_key]

    def __setitem__(self, key, value):
        """
        Sets the value associated with the given key (underscore_case).

        Args:
            key (str): The key to set (in underscore_case).
            value: The value to associate with the camelCase version of the key.
        """
        camel_case_key = self._convert_key(key)
        self._data[camel_case_key] = value

    def __delitem__(self, key):
        """
        Deletes the item associated with the given key (underscore_case).

        Args:
            key (str): The key to delete (in underscore_case).

        Raises:
            KeyError: If the camelCase key is not found.
        """
        camel_case_key = self._convert_key(key)
        del self._data[camel_case_key]

    def __contains__(self, key):
        """
        Checks if the given key (underscore_case) exists in the map.

        Args:
            key (str): The key to check (in underscore_case).

        Returns:
            bool: True if the camelCase version of the key exists, False otherwise.
        """
        camel_case_key = self._convert_key(key)
        return camel_case_key in self._data

    def __iter__(self):
        """
        Returns an iterator over the camelCase keys in the map.
        """
        return iter(self._data)

    def __len__(self):
        """
        Returns the number of items in the map.
        """
        return len(self._data)

    def _convert_key(self, key):
        """
        Converts an underscore_case key to camelCase.

        Args:
            key (str): The key to convert.

        Returns:
            str: The camelCase version of the key.
        """
        return self._to_camel_case(key)

    @staticmethod
    def _to_camel_case(key):
        """
        Converts an underscore_case string to camelCase.

        Args:
            key (str): The string to convert.

        Returns:
            str: The camelCase version of the string.
        """
        components = key.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])