class ArgumentParser:
    """
    A class for parsing command line arguments into a dictionary.
    """

    def __init__(self):
        """
        Initializes the parser with empty arguments, required arguments, and types.
        """
        self.arguments = {}
        self.required = set()
        self.types = {}

    def parse_arguments(self, command_string):
        """
        Parses the command line arguments and stores them in the arguments dictionary.
        Checks for missing required arguments and returns their names if any are missing.

        :param command_string: str, command line argument string
        :return: tuple (bool, set or None)
        """
        parts = command_string.split()
        if len(parts) < 2:
            return False, self.required

        for part in parts[2:]:  # Skip the first two parts (script name)
            if '=' in part:
                arg, value = part.split('=', 1)
            else:
                arg = part
                value = True  # Boolean flag

            arg = arg.lstrip('-')

            # Store the argument value with type conversion
            self.arguments[arg] = self._convert_type(arg, value)

        missing_args = self.required - self.arguments.keys()
        return (True, None) if not missing_args else (False, missing_args)

    def get_argument(self, key):
        """
        Retrieves the value of the specified argument.

        :param key: str, argument name
        :return: The value of the argument, or None if not found.
        """
        return self.arguments.get(key)

    def add_argument(self, arg, required=False, arg_type=str):
        """
        Adds an argument to the parser's expected arguments.

        :param arg: str, argument name
        :param required: bool, whether the argument is required
        :param arg_type: type, expected type of the argument
        """
        self.types[arg] = arg_type
        if required:
            self.required.add(arg)

    def _convert_type(self, arg, value):
        """
        Converts the value to the expected type if applicable.

        :param arg: str, argument name
        :param value: str, value to convert
        :return: converted value or original value if conversion fails
        """
        if arg in self.types:
            try:
                return self.types[arg](value)
            except ValueError:
                return value  # Return original value if conversion fails
        return value