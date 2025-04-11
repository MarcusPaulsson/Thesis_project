from itertools import permutations

a = input().strip()
b = input().strip()

# Generate all unique permutations of the digits of a
perms = sorted(set(''.join(p) for p in permutations(a)), reverse=True)

# Find the maximum permutation that is less than or equal to b
for perm in perms:
    if perm <= b:
        print(perm)
        break