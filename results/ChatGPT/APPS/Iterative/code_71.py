def count_set_bits(n):
    return bin(n).count('1')

if __name__ == "__main__":
    a = int(input("Enter an integer between 1 and 64: "))
    if 1 <= a <= 64:
        print(count_set_bits(a))
    else:
        print("Input must be between 1 and 64.")