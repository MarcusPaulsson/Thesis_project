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
        Parses the given command line argument string and stores the parsed result in the arguments dictionary.
        Checks for missing required arguments, if any, and returns False with the missing argument names, otherwise returns True.
        :param command_string: str, command line argument string, formatted like "python script.py --arg1=value1 -arg2 value2 --option1 -option2"
        :return tuple: (True, None) if parsing is successful, (False, missing_args) if parsing fails,
            where missing_args is a set of the missing argument names which are str.
        """
        args = command_string.split()
        i = 0
        while i < len(args):
            arg = args[i]
            if arg.startswith("--"):
                arg_name = arg[2:].split("=")[0]
                if "=" in arg:
                    arg_value = arg[2:].split("=")[1]
                    self.arguments[arg_name] = self._convert_type(arg_name, arg_value)
                else:
                    self.arguments[arg_name] = True
            elif arg.startswith("-"):
                arg_name = arg[1:]
                if i + 1 < len(args) and not args[i + 1].startswith("-"):
                    arg_value = args[i + 1]
                    self.arguments[arg_name] = self._convert_type(arg_name, arg_value)
                    i += 1
                else:
                    self.arguments[arg_name] = True
            i += 1

        missing_args = self.required - set(self.arguments.keys())
        if missing_args:
            return False, missing_args
        else:
            return True, None

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
        If the argument is set as required, it will be added to the required set.
        The argument type and name are stored in the types dictionary as key-value pairs.
        :param arg: str, argument name
        :param required: bool, whether the argument is required, default is False
        :param arg_type:str, Argument type, default is str
        """
        if required:
            self.required.add(arg)
        self.types[arg] = arg_type

    def _convert_type(self, arg, value):
        """
        Try to convert the type of input value by searching in self.types.
        :param value: str, the input value in command line
        :return: return corresponding value in self.types if convert successfully, or the input value otherwise
        """
        arg_type = self.types.get(arg)
        if arg_type:
            try:
                if arg_type == int:
                    return int(value)
                elif arg_type == float:
                    return float(value)
                elif arg_type == bool:
                    return value.lower() == 'true' or value.lower() == '1' or value == ''
                else:
                    return value
            except ValueError:
                return value
        else:
            return value