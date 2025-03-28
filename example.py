
import os
import json
import datetime

class hello:
    def __init__(self):
        print("hello")

    def print_hello(self):
        print("hello")

    def print_hello_world(self):
        print("hello world")


def try_print_hello(value):
    print("hello") if value else print("world")

print("Hello, world!")
current_time = datetime.datetime.now()
file_path = os.path.join("data", "file.txt")
my_list = [3, 1, 4, 1, 5, 9, 2, 6]
my_list.sort()
my_string = "hello"
my_string.upper()
data = json.dumps({"key": "value"})

hello_instance = hello()
hello_instance.print_hello()
hello_instance.print_hello_world()


try_print_hello(True)
try_print_hello(False)
