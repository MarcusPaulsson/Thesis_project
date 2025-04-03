from itertools import permutations

a = input().strip()
b = input().strip()

# Generate all unique permutations of digits of a
permuted_numbers = sorted(set(int(''.join(p)) for p in permutations(a)), reverse=True)

# Find the maximum permutation that is less than or equal to b
max_number = None
for num in permuted_numbers:
    if num <= int(b):
        max_number = num
        break

print(max_number)