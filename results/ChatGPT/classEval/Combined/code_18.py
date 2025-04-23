class CamelCaseMap:
    """
    A custom class that allows keys to be in camel case style by converting them from underscore style,
    providing dictionary-like functionality.
    """

    def __init__(self):
        """Initialize data to an empty dictionary."""
        self._data = {}

    def __getitem__(self, key):
        """Return the value corresponding to the key."""
        key = self._convert_key(key)
        return self._data.get(key)

    def __setitem__(self, key, value):
        """Set the value corresponding to the key to the specified value."""
        key = self._convert_key(key)
        self._data[key] = value

    def __delitem__(self, key):
        """Delete the value corresponding to the key."""
        key = self._convert_key(key)
        self._data.pop(key, None)  # Safely remove the key if it exists

    def __iter__(self):
        """Return an iterator over the keys in camel case."""
        return (self._to_camel_case(key) for key in self._data.keys())

    def __len__(self):
        """Return the length of the data."""
        return len(self._data)

    def _convert_key(self, key):
        """Convert key string into camel case if it's a string."""
        if isinstance(key, str):
            return self._to_camel_case(key)
        return key

    @staticmethod
    def _to_camel_case(key):
        """Convert key string into camel case."""
        parts = key.split('_')
        return parts[0] + ''.join(part.capitalize() for part in parts[1:])