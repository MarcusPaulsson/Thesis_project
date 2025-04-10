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
        """
        command_parts = command_string.split()[1:]  # Ignore the script name
        missing_args = set()
        parsed_args = {}

        for part in command_parts:
            if '=' in part:
                arg, value = part.split('=', 1)
            else:
                arg = part
                value = True  # Treat flag as True if no value is provided

            if arg.startswith('--'):
                arg_name = arg[2:]
            elif arg.startswith('-'):
                arg_name = arg[1:]
            else:
                continue

            if arg_name in self.types:
                parsed_args[arg_name] = self._convert_type(arg_name, value)
            else:
                parsed_args[arg_name] = value

        # Check for required arguments
        for req in self.required:
            if req not in parsed_args:
                missing_args.add(req)

        self.arguments.update(parsed_args)

        return (len(missing_args) == 0, missing_args if missing_args else None)

    def get_argument(self, key):
        """
        Retrieves the value of the specified argument from the arguments dictionary and returns it.
        :param key: str, argument name
        :return: The value of the argument, or None if the argument does not exist.
        """
        return self.arguments.get(key)

    def add_argument(self, arg, required=False, arg_type=str):
        """
        Adds an argument to self.types and self.required.
        Check if it is a required argument and store the argument type.
        If the argument is set as required, it will be added to the required set.
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
        :return: return corresponding value in self.types if convert successfully, or the input value otherwise
        """
        try:
            return self.types[arg](value)
        except (ValueError, TypeError):
            return value