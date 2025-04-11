def count_set_bits(n):
    return bin(n).count('1')

a = int(input())
print(count_set_bits(a))