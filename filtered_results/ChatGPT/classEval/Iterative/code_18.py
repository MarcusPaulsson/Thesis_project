class CamelCaseMap:
    """
    A custom class that allows keys to be in camel case style by converting them from underscore style, providing dictionary-like functionality.
    """

    def __init__(self):
        """Initialize data to an empty dictionary."""
        self._data = {}

    def __getitem__(self, key):
        """Return the value corresponding to the key."""
        key = self._convert_key(key)
        return self._data[key]

    def __setitem__(self, key, value):
        """Set the value corresponding to the key to the specified value."""
        key = self._convert_key(key)
        self._data[key] = value

    def __delitem__(self, key):
        """Delete the value corresponding to the key."""
        key = self._convert_key(key)
        del self._data[key]

    def __iter__(self):
        """Return an iterator for the keys in camel case format."""
        return iter(self._data)

    def __len__(self):
        """Return the number of items in the map."""
        return len(self._data)

    def _convert_key(self, key):
        """Convert the key string into camel case."""
        if isinstance(key, str):
            return self._to_camel_case(key)
        return key

    @staticmethod
    def _to_camel_case(key):
        """Convert the key string into camel case."""
        parts = key.split('_')
        return parts[0] + ''.join(part.capitalize() for part in parts[1:])

    def __contains__(self, key):
        """Check if a key exists in the map, considering camel case variations."""
        converted_key = self._convert_key(key)
        return converted_key in self._data