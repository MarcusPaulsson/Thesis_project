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
        >>> parser = ArgumentParser()
        >>> parser.arguments
        {}
        >>> parser.required
        set()
        >>> parser.types
        {}
        """
        self.arguments = {}
        self.required = set()
        self.types = {}

    def parse_arguments(self, command_string):
        """
        Parses the given command line argument string and invoke _convert_type to stores the parsed result in specific type in the arguments dictionary.
        Checks for missing required arguments, if any, and returns False with the missing argument names, otherwise returns True.
        :param command_string: str, command line argument string, formatted like "python script.py --arg1=value1 -arg2 value2 --option1 -option2"
        :return tuple: (True, None) if parsing is successful, (False, missing_args) if parsing fails,
            where missing_args is a set of the missing argument names which are str.
        >>> parser = ArgumentParser()
        >>> parser.add_argument("arg1", True, "str")
        >>> parser.add_argument("arg2", False, "str")
        >>> parser.add_argument("option1", False, "bool")
        >>> parser.parse_arguments("python script.py --arg1=value1 -arg2 value2 --option1 -option2")
        (True, None)
        >>> parser.arguments
        {'arg1': 'value1', 'arg2': 'value2', 'option1': True, 'option2': True}
        """
        import shlex
        args = shlex.split(command_string)
        for arg in args[2:]:  # Skip the "python script.py" part
            if '=' in arg:
                key, value = arg.split('=', 1)
            else:
                key = arg
                value = True  # For flags

            key = key.lstrip('-')  # Remove leading dashes
            if key not in self.types:
                continue

            self.arguments[key] = self._convert_type(key, value)

        missing_args = self.required - self.arguments.keys()
        return (len(missing_args) == 0, missing_args if missing_args else None)

    def get_argument(self, key):
        """
        Retrieves the value of the specified argument from the arguments dictionary and returns it.
        :param key: str, argument name
        :return: The value of the argument, or None if the argument does not exist.
        >>> parser = ArgumentParser()
        >>> parser.add_argument('arg1', True, 'str')
        >>> parser.parse_arguments("python script.py --arg1=value1")
        >>> parser.get_argument('arg1')
        'value1'
        >>> parser.get_argument('arg2')
        >>> parser.get_argument('nonexistent')
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
        >>> parser = ArgumentParser()
        >>> parser.add_argument('arg1', True, int)
        >>> parser.required
        {'arg1'}
        >>> parser.types
        {'arg1': int}
        """
        self.types[arg] = arg_type
        if required:
            self.required.add(arg)

    def _convert_type(self, arg, value):
        """
        Try to convert the type of input value by searching in self.types.
        :param value: str, the input value in command line
        :return: return corresponding value in self.types if convert successfully, or the input value otherwise
        >>> parser = ArgumentParser()
        >>> parser.types = {'arg1': int}
        >>> parser._convert_type('arg1', '21')
        21
        >>> parser._convert_type('arg1', 'hello')
        'hello'
        """
        arg_type = self.types.get(arg, str)
        try:
            return arg_type(value) if arg_type is not bool else True
        except (ValueError, TypeError):
            return value