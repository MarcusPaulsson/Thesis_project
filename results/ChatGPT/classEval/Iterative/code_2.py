class ArgumentParser:
    """
    A class for parsing command line arguments into a dictionary.
    """

    def __init__(self):
        """
        Initialize the fields.
        self.arguments is a dict that stores the args from the command line.
        self.required is a set that stores the required arguments.
        self.types is a dict that stores the type of each argument.
        """
        self.arguments = {}
        self.required = set()
        self.types = {}

    def parse_arguments(self, command_string):
        """
        Parses the given command line argument string and stores the parsed result in
        specific types in the arguments dictionary. Checks for missing required arguments,
        returning False with the missing argument names if any, otherwise returns True.
        :param command_string: str, command line argument string formatted like
            "python script.py --arg1=value1 -arg2 value2 --option1 -option2"
        :return tuple: (True, None) if parsing is successful, (False, missing_args) if parsing fails,
            where missing_args is a set of the missing argument names which are str.
        """
        args = command_string.split()[1:]  # Skip the script name
        missing_args = set(self.required)

        for arg in args:
            if '=' in arg:
                key, value = arg.split('=', 1)  # Split only on the first '='
            else:
                key = arg
                value = True  # For flags

            key = key.lstrip('-')  # Remove leading dashes

            if key in self.types:
                value = self._convert_type(key, value)

            self.arguments[key] = value

            if key in missing_args:
                missing_args.remove(key)

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
        Adds an argument to self.types and self.required.
        If the argument is required, it will be added to the required set.
        The argument type and name are stored in the types dictionary as key-value pairs.
        :param arg: str, argument name
        :param required: bool, whether the argument is required, default is False
        :param arg_type: type, Argument type, default is str
        """
        self.types[arg] = arg_type
        if required:
            self.required.add(arg)

    def _convert_type(self, arg, value):
        """
        Try to convert the type of input value by searching in self.types.
        :param value: str, the input value in command line
        :return: value converted to the corresponding type in self.types if conversion succeeds,
            or the input value otherwise.
        """
        if arg in self.types:
            try:
                return self.types[arg](value)
            except (ValueError, TypeError):
                pass
        return value