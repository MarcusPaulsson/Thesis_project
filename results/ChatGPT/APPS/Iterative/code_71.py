try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("Input must be a positive integer.")
    output = (a - 1).bit_length()
    print(output)
except ValueError as e:
    print(e)