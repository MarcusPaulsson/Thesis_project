def count_set_bits(n):
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count

if __name__ == "__main__":
    a = int(input().strip())
    print(count_set_bits(a))