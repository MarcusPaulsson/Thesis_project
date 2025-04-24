class ArgumentParser:
    """
    A class for parsing command line arguments into a dictionary.
    """

    def __init__(self):
        """
        Initializes the fields:
        - self.arguments: a dict that stores the parsed command line arguments.
        - self.required: a set that stores the names of required arguments.
        - self.types: a dict that stores the expected types for each argument.
        """
        self.arguments = {}
        self.required = set()
        self.types = {}

    def parse_arguments(self, command_string):
        """
        Parses the given command line argument string and stores the parsed results in the arguments dictionary.
        Checks for missing required arguments and returns a tuple indicating success and any missing arguments.
        
        :param command_string: str, command line argument string formatted like "python script.py --arg1=value1 -arg2 value2 --option1 -option2"
        :return: tuple (bool, set or None) indicating success and missing arguments if any.
        """
        args = command_string.split()[1:]  # Skip the script name
        missing_args = set()

        for arg in args:
            key, value = self._parse_arg(arg)
            self.arguments[key] = self._convert_type(key, value)

        for req in self.required:
            if req not in self.arguments:
                missing_args.add(req)

        return (not missing_args, missing_args if missing_args else None)

    def get_argument(self, key):
        """
        Retrieves the value of the specified argument from the arguments dictionary.
        
        :param key: str, argument name
        :return: The value of the argument, or None if the argument does not exist.
        """
        return self.arguments.get(key)

    def add_argument(self, arg, required=False, arg_type=str):
        """
        Adds an argument to the parser, specifying if it is required and its expected type.
        
        :param arg: str, argument name
        :param required: bool, whether the argument is required, default is False
        :param arg_type: type, expected type of the argument, default is str
        """
        self.types[arg] = arg_type
        if required:
            self.required.add(arg)

    def _convert_type(self, arg, value):
        """
        Converts the input value to the expected type based on the argument's type.
        
        :param arg: str, the argument name
        :param value: str, the input value from the command line
        :return: converted value if successful, or the original value otherwise
        """
        if arg in self.types:
            try:
                return self.types[arg](value)
            except ValueError:
                pass
        return value

    def _parse_arg(self, arg):
        """
        Parses a single argument string into a key and value.
        
        :param arg: str, the argument string
        :return: tuple (str, str) containing the key and value
        """
        if '=' in arg:
            key, value = arg.split('=', 1)
        else:
            key = arg
            value = True  # Treat flags as True

        key = key.lstrip('-')  # Remove leading dashes
        return key, value