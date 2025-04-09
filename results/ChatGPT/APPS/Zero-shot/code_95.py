n = int(input())
s = input().strip()
t = input().strip()

# Create a list of characters
chars = ['a'] * n + ['b'] * n + ['c'] * n

# Function to check if a string contains substrings s or t
def contains_substring(res):
    return s in res or t in res

# Try to generate a valid string
from itertools import permutations

# Generate all permutations of the string
for perm in permutations(chars):
    res = ''.join(perm)
    if not contains_substring(res):
        print("YES")
        print(res)
        break
else:
    print("NO")