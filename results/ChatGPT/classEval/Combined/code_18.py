class CamelCaseMap:
    """
    Custom class that allows keys to be in camel case style by converting them 
    from underscore style, providing dictionary-like functionality.
    """

    def __init__(self):
        """Initialize data to an empty dictionary."""
        self._data = {}

    def __getitem__(self, key):
        """Return the value corresponding to the key."""
        return self._data[self._convert_key(key)]

    def __setitem__(self, key, value):
        """Set the value corresponding to the key."""
        self._data[self._convert_key(key)] = value

    def __delitem__(self, key):
        """Delete the value corresponding to the key."""
        del self._data[self._convert_key(key)]

    def __iter__(self):
        """Return an iterator over the keys of the dictionary."""
        return iter(self._data)

    def __len__(self):
        """Return the length of the dictionary."""
        return len(self._data)

    def _convert_key(self, key):
        """Convert key string into camel case."""
        if not isinstance(key, str):
            return key
        return self._to_camel_case(key)

    @staticmethod
    def _to_camel_case(key):
        """Convert key string into camel case."""
        parts = key.split('_')
        return parts[0] + ''.join(part.capitalize() for part in parts[1:])