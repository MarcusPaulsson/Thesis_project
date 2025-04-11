a = int(input())
if 1 <= a <= 64:
    output = (a - 1).bit_length()
    print(output)
else:
    print("Input must be between 1 and 64.")