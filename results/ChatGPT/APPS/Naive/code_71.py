def calculate_output(a):
    return (a - 1).bit_length()

a = int(input())
print(calculate_output(a))