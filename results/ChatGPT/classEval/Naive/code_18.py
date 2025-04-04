class CamelCaseMap:
    """
    This is a custom class that allows keys to be in camel case style by converting them from underscore style, which provides dictionary-like functionality.
    """

    def __init__(self):
        """Initialize data to an empty dictionary."""
        self._data = {}

    def __getitem__(self, key):
        """Return the value corresponding to the key."""
        return self._data[self._convert_key(key)]

    def __setitem__(self, key, value):
        """Set the value corresponding to the key to the specified value."""
        self._data[self._convert_key(key)] = value

    def __delitem__(self, key):
        """Delete the value corresponding to the key."""
        del self._data[self._convert_key(key)]

    def __iter__(self):
        """Return an iterator over the keys."""
        return iter(self._data)

    def __len__(self):
        """Return the length of the data."""
        return len(self._data)

    def _convert_key(self, key):
        """Convert key string into camel case."""
        return self._to_camel_case(key)

    @staticmethod
    def _to_camel_case(key):
        """Convert key string into camel case."""
        components = key.split('_')
        return components[0] + ''.join(word.capitalize() for word in components[1:])