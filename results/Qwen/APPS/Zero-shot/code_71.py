def count_bits(a):
    return bin(a).count('1')

a = int(input())
print(count_bits(a))