class ArgumentParser:
    """
    This is a class for parsing command line arguments to a dictionary.
    """

    def __init__(self):
        """
        Initialize the fields.
        self.arguments is a dict that stores the args in a command line
        self.required is a set that stores the required arguments
        self.types is a dict that stores type of every arguments.
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
        """
        import shlex
        
        args = shlex.split(command_string)
        for arg in args[2:]:
            if '=' in arg:
                key, value = arg.split('=', 1)
            else:
                key = arg
                value = True
            
            # Normalize the key
            key = key.lstrip('-')
            self.arguments[key] = self._convert_type(key, value)

        missing_args = self.required - self.arguments.keys()
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
        if required:
            self.required.add(arg)
        self.types[arg] = arg_type

    def _convert_type(self, arg, value):
        """
        Try to convert the type of input value by searching in self.types.
        :param arg: str, the argument name
        :param value: str, the input value in command line
        :return: return corresponding value in self.types if convert successfully, or the input value otherwise
        """
        if arg in self.types:
            try:
                return self.types[arg](value)
            except ValueError:
                return value
        return value