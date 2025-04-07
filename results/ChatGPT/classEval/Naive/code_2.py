class ArgumentParser:
    """
    This is a class for parsing command line arguments to a dictionary.
    """

    def __init__(self):
        """
        Initialize the fields.
        self.arguments is a dict that stores the args in a command line
        self.requried is a set that stores the required arguments
        self.types is a dict that stores type of every arguments.
        >>> parser.arguments
        {'key1': 'value1', 'option1': True}
        >>> parser.required
        {'arg1'}
        >>> parser.types
        {'arg1': 'type1'}
        """
        self.arguments = {}
        self.required = set()
        self.types = {}

    def parse_arguments(self, command_string):
        """
        Parses the given command line argument string and invokes _convert_type to store the parsed result in specific type in the arguments dictionary.
        Checks for missing required arguments, if any, and returns False with the missing argument names, otherwise returns True.
        :param command_string: str, command line argument string, formatted like "python script.py --arg1=value1 -arg2 value2 --option1 -option2"
        :return tuple: (True, None) if parsing is successful, (False, missing_args) if parsing fails,
            where missing_args is a set of the missing argument names which are str.
        >>> parser.parse_arguments("python script.py --arg1=value1 -arg2 value2 --option1 -option2")
        (True, None)
        >>> parser.arguments
        {'arg1': 'value1', 'arg2': 'value2', 'option1': True, 'option2': True}
        """
        command_parts = command_string.split()
        for part in command_parts[1:]:  # Skip the script name
            if '=' in part:
                key, value = part.split('=', 1)
            else:
                if part.startswith('-'):
                    key = part.lstrip('-')
                    value = True
                else:
                    raise ValueError("Invalid argument format")

            if key.startswith('--'):
                key = key[2:]
            elif key.startswith('-'):
                key = key[1:]

            converted_value = self._convert_type(key, value)
            self.arguments[key] = converted_value

        missing_args = self.required - self.arguments.keys()
        if missing_args:
            return False, missing_args

        return True, None

    def get_argument(self, key):
        """
        Retrieves the value of the specified argument from the arguments dictionary and returns it.
        :param key: str, argument name
        :return: The value of the argument, or None if the argument does not exist.
        >>> parser.arguments
        {'arg1': 'value1', 'arg2': 'value2', 'option1': True, 'option2': True}
        >>> parser.get_argument('arg2')
        'value2'
        """
        return self.arguments.get(key, None)

    def add_argument(self, arg, required=False, arg_type=str):
        """
        Adds an argument to self.types and self.required.
        Check if it is a required argument and store the argument type.
        If the argument is set as required, it will be added to the required set.
        The argument type and name are stored in the types dictionary as key-value pairs.
        :param arg: str, argument name
        :param required: bool, whether the argument is required, default is False
        :param arg_type: type, Argument type, default is str
        >>> parser.add_argument('arg1', True, int)
        >>> parser.required
        {'arg1'}
        >>> parser.types
        {'arg1': int}
        """
        if required:
            self.required.add(arg)
        self.types[arg] = arg_type

    def _convert_type(self, arg, value):
        """
        Try to convert the type of input value by searching in self.types.
        :param value: str, the input value in command line
        :return: return corresponding value in self.types if converted successfully, or the input value otherwise
        >>> parser.types
        {'arg1': int}
        >>> parser._convert_type('arg1', '21')
        21
        """
        if arg in self.types:
            try:
                return self.types[arg](value)
            except (ValueError, TypeError):
                pass
        return value