class CamelCaseMap:
    """
    A custom class that allows keys to be stored in camel case style 
    by converting them from underscore style, providing dictionary-like functionality.
    """

    def __init__(self):
        """Initialize data to an empty dictionary."""
        self._data = {}

    def __getitem__(self, key):
        """Return the value corresponding to the key."""
        key = self._to_camel_case(key)
        return self._data.get(key)

    def __setitem__(self, key, value):
        """Set the value for the given key."""
        key = self._to_camel_case(key)
        self._data[key] = value

    def __delitem__(self, key):
        """Delete the value corresponding to the key."""
        key = self._to_camel_case(key)
        if key in self._data:
            del self._data[key]
        else:
            raise KeyError(f"Key '{key}' not found.")

    def __iter__(self):
        """Return an iterator over the keys of the dictionary."""
        return iter(self._data)

    def __len__(self):
        """Return the number of items in the dictionary."""
        return len(self._data)

    @staticmethod
    def _to_camel_case(key):
        """Convert a string from underscore to camel case."""
        if not isinstance(key, str):
            return key
        components = key.split('_')
        return components[0] + ''.join(x.capitalize() for x in components[1:])

    def _convert_key(self, key):
        """Convert the input key to camel case."""
        return self._to_camel_case(key)