def find_integer(a):
    return (a - 1).bit_length()

if __name__ == "__main__":
    a = int(input().strip())
    print(find_integer(a))