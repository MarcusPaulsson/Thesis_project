n = int(input())
s = input().strip()
t = input().strip()

# Create a list of characters to use in the result
result = ['a'] * n + ['b'] * n + ['c'] * n

# Function to check if the current result contains forbidden substrings
def contains_forbidden_substrings(res, s, t):
    return s in res or t in res

# Try to generate a valid string
from itertools import permutations

# Generate all permutations of the result
for perm in permutations(result):
    res = ''.join(perm)
    if not contains_forbidden_substrings(res, s, t):
        print("YES")
        print(res)
        break
else:
    print("NO")