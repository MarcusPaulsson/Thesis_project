class ArgumentParser:
    """
    A class for parsing command line arguments into a dictionary.
    """

    def __init__(self):
        """
        Initializes the fields for arguments, required arguments, and types.
        """
        self.arguments = {}
        self.required = set()
        self.types = {}

    def parse_arguments(self, command_string):
        """
        Parses the given command line argument string and stores the parsed result.
        Checks for missing required arguments, if any, and returns a tuple indicating success and missing arguments.
        
        :param command_string: str, command line argument string formatted like "python script.py --arg1=value1 -arg2 value2 --option1 -option2"
        :return: tuple (bool, set or None) indicating success and missing arguments
        """
        command_string = command_string.strip().split()
        for arg in command_string[1:]:  # Skip the script name
            if '=' in arg:
                key, value = arg.split('=', 1)
            else:
                key, value = arg, None
            
            if key.startswith('--'):
                key = key[2:]
                self.arguments[key] = True if value is None else self._convert_type(key, value)
            elif key.startswith('-'):
                key = key[1:]
                self.arguments[key] = True

        # Check for missing required arguments
        missing_args = self.required - self.arguments.keys()
        return (len(missing_args) == 0, missing_args if missing_args else None)

    def get_argument(self, key):
        """
        Retrieves the value of the specified argument from the arguments dictionary.
        
        :param key: str, argument name
        :return: The value of the argument or None if it does not exist.
        """
        return self.arguments.get(key)

    def add_argument(self, arg, required=False, arg_type=str):
        """
        Adds an argument to self.types and self.required.
        
        :param arg: str, argument name
        :param required: bool, whether the argument is required, default is False
        :param arg_type: type, Argument type, default is str
        """
        if required:
            self.required.add(arg)
        self.types[arg] = arg_type

    def _convert_type(self, arg, value):
        """
        Tries to convert the input value to the specified type based on self.types.
        
        :param arg: str, argument name
        :param value: str, the input value from command line
        :return: converted value if successful, otherwise returns the input value
        """
        if arg in self.types:
            try:
                return self.types[arg](value)
            except ValueError:
                pass
        return value