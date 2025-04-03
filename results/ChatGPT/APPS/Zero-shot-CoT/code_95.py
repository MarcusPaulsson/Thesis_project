def generate_string(n, s, t):
    # Create the base string with n 'a's, n 'b's, and n 'c's
    base = 'a' * n + 'b' * n + 'c' * n
    
    # Check for the two substrings s and t, and try to avoid them
    # If s or t is made of the same characters, we can directly rearrange
    if s[0] == s[1] or t[0] == t[1]:
        # Simply shuffle the base string
        res = base
        print("YES")
        print(res)
        return
    
    def is_valid(res):
        return s not in res and t not in res

    # Try to generate a valid string by shuffling
    from itertools import permutations
    
    for perm in permutations(base):
        res = ''.join(perm)
        if is_valid(res):
            print("YES")
            print(res)
            return
    
    print("NO")

# Reading input
n = int(input().strip())
s = input().strip()
t = input().strip()

generate_string(n, s, t)