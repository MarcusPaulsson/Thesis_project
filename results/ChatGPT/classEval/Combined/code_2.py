class ArgumentParser:
    """
    A class for parsing command line arguments into a dictionary.
    """

    def __init__(self):
        self.arguments = {}
        self.required = set()
        self.types = {}

    def parse_arguments(self, command_string):
        """
        Parses the command line argument string and stores the parsed results in the arguments dictionary.
        Checks for missing required arguments and returns a tuple indicating success and any missing arguments.
        
        :param command_string: str, command line argument string formatted like "python script.py --arg1=value1 -arg2 value2 --option1 -option2"
        :return: tuple: (True, None) if parsing is successful, (False, missing_args) if parsing fails,
            where missing_args is a set of the missing argument names.
        """
        tokens = command_string.split()
        for token in tokens[1:]:  # Skip the script name
            key, value = self._parse_token(token)
            key = key.lstrip('-')  # Remove leading dashes

            if key in self.types:
                self.arguments[key] = self._convert_type(key, value)
            else:
                self.arguments[key] = value

        missing_args = {arg for arg in self.required if arg not in self.arguments}
        return (len(missing_args) == 0, missing_args if missing_args else None)

    def get_argument(self, key):
        """
        Retrieves the value of the specified argument from the arguments dictionary.

        :param key: str, argument name
        :return: The value of the argument, or None if the argument does not exist.
        """
        return self.arguments.get(key)

    def add_argument(self, arg, required=False, arg_type=str):
        """
        Adds an argument to the parser, specifying its type and whether it's required.

        :param arg: str, argument name
        :param required: bool, whether the argument is required
        :param arg_type: type, expected type for the argument value
        """
        self.types[arg] = arg_type
        if required:
            self.required.add(arg)

    def _convert_type(self, arg, value):
        """
        Converts the value to the specified type for the argument.

        :param arg: str, argument name
        :param value: str, the input value in command line
        :return: Converted value if successful, otherwise the input value
        """
        try:
            return self.types[arg](value)
        except (ValueError, TypeError):
            return value

    def _parse_token(self, token):
        """
        Parses a single token from the command line, separating key and value.

        :param token: str, command line token
        :return: tuple: (key, value)
        """
        if '=' in token:
            key, value = token.split('=', 1)
        else:
            key = token
            value = True  # For flags, set value to True
        return key, value