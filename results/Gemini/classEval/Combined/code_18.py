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
        Retrieves the value associated with the given key.

        Args:
            key (str): The key to retrieve the value for (can be in underscore_case or camelCase).

        Returns:
            The value associated with the key.

        Raises:
            KeyError: If the key is not found in the map.
        """
        camel_key = self._convert_key(key)
        return self._data[camel_key]

    def __setitem__(self, key, value):
        """
        Sets the value associated with the given key.

        Args:
            key (str): The key to set the value for (can be in underscore_case or camelCase).
            value: The value to associate with the key.
        """
        camel_key = self._convert_key(key)
        self._data[camel_key] = value

    def __delitem__(self, key):
        """
        Deletes the key-value pair associated with the given key.

        Args:
            key (str): The key to delete (can be in underscore_case or camelCase).

        Raises:
            KeyError: If the key is not found in the map.
        """
        camel_key = self._convert_key(key)
        del self._data[camel_key]

    def __contains__(self, key):
        """
        Checks if the map contains the given key.

        Args:
            key (str): The key to check for (can be in underscore_case or camelCase).

        Returns:
            True if the map contains the key, False otherwise.
        """
        camel_key = self._convert_key(key)
        return camel_key in self._data

    def __iter__(self):
        """
        Returns an iterator over the keys in the map.

        Returns:
            An iterator over the keys in the map (in camelCase).
        """
        return iter(self._data)

    def __len__(self):
        """
        Returns the number of key-value pairs in the map.

        Returns:
            The number of key-value pairs in the map.
        """
        return len(self._data)

    def _convert_key(self, key):
        """
        Converts a key from underscore_case to camelCase if it's a string.

        Args:
            key: The key to convert.

        Returns:
            The converted key (in camelCase) if it was a string, otherwise the original key.
        """
        if isinstance(key, str):
            return self._to_camel_case(key)
        return key

    @staticmethod
    def _to_camel_case(key):
        """
        Converts a string from underscore_case to camelCase.

        Args:
            key (str): The string to convert.

        Returns:
            The converted string (in camelCase).
        """
        components = key.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])