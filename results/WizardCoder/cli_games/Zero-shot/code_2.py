class ArgumentParser:
    def __init__(self):
        self.arguments = {}
        self.required = set()
        self.types = {}

    def parse_arguments(self, command_string):
        args = command_string.split(" ")
        for arg in args:
            if arg.startswith('--'):
                key, value = arg[2:].split('=')
                self._add_to_dict(key, value, required=False)
            elif arg.startswith('-'):
                key = arg[1:]
                if key in self.types:
                    self._add_to_dict(key, True, required=False)
        return True, None

    def get_argument(self, key):
        return self.arguments.get(key, None)

    def add_argument(self, arg, required=False, arg_type=str):
        if arg_type == 'int':
            self.types[arg] = int
        else:
            self.types[arg] = str
        if required:
            self.required.add(arg)

    def _add_to_dict(self, key, value, required=False):
        try:
            arg_type = self.types.get(key, None)
            if arg_type is not None:
                self.arguments[key] = arg_type(value)
            else:
                self.arguments[key] = value
        except ValueError:
            print("Invalid argument type")