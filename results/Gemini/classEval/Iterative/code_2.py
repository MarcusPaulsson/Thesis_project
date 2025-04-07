class ArgumentParser:
    """
    A class for parsing command line arguments into a dictionary.
    """

    def __init__(self):
        """
        Initializes the ArgumentParser with empty dictionaries for arguments and types,
        and an empty set for required arguments.
        """
        self.arguments = {}
        self.required = set()
        self.types = {}

    def parse_arguments(self, command_string):
        """
        Parses a command line argument string.

        Args:
            command_string: The command line argument string (e.g., "python script.py --arg1=value1 -arg2 value2 --option1 -option2").

        Returns:
            A tuple: (True, None) if parsing succeeds, or (False, missing_args) if parsing fails,
            where missing_args is a set of missing required argument names.
        """
        args = command_string.split()
        i = 0
        while i < len(args):
            arg = args[i]
            if arg.startswith('--'):
                arg_name = arg[2:]
                if '=' in arg_name:
                    arg_name, arg_value = arg_name.split('=', 1)  # Split only once
                    self.arguments[arg_name] = self._convert_type(arg_name, arg_value)
                elif i + 1 < len(args) and not args[i + 1].startswith('-'):
                    i += 1
                    self.arguments[arg_name] = self._convert_type(arg_name, args[i])
                else:
                    self.arguments[arg_name] = True
            elif arg.startswith('-'):
                arg_name = arg[1:]
                if i + 1 < len(args) and not args[i + 1].startswith('-'):
                    i += 1
                    self.arguments[arg_name] = self._convert_type(arg_name, args[i])
                else:
                    self.arguments[arg_name] = True
            i += 1

        missing_args = self.required - set(self.arguments.keys())

        if missing_args:
            return False, missing_args
        else:
            return True, None

    def get_argument(self, key, default=None):
        """
        Retrieves the value of the specified argument.

        Args:
            key: The argument name.
            default: The default value to return if the argument is not found (default: None).

        Returns:
            The value of the argument or the default value if the argument is not found.
        """
        return self.arguments.get(key, default)

    def add_argument(self, arg, required=False, arg_type=str):
        """
        Adds an argument definition.

        Args:
            arg: The argument name.
            required: Whether the argument is required (default: False).
            arg_type: The argument type (default: str).
        """
        self.types[arg] = arg_type
        if required:
            self.required.add(arg)

    def _convert_type(self, arg, value):
        """
        Converts a value to the specified type for an argument.

        Args:
            arg: The argument name.
            value: The value to convert.

        Returns:
            The converted value, or the original value if no conversion is possible.
        """
        arg_type = self.types.get(arg)
        if arg_type:
            try:
                if arg_type == int or arg_type == 'int':
                    return int(value)
                elif arg_type == float or arg_type == 'float':
                    return float(value)
                elif arg_type == bool or arg_type == 'bool':
                    value = value.lower()
                    if value == 'true':
                        return True
                    elif value == 'false':
                        return False
                    else:
                        return value  # Or raise an exception for invalid boolean values
                else:
                    return str(value) # Explicitly convert to string for consistency
            except ValueError:
                return value
        return value