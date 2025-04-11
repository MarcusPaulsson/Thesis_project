def count_set_bits(n):
    return bin(n).count('1')

if __name__ == "__main__":
    a = int(input().strip())
    if 1 <= a <= 64:
        print(count_set_bits(a))
    else:
        raise ValueError("Input must be between 1 and 64 inclusive.")