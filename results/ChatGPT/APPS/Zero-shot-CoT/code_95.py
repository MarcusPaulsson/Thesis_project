def generate_string(n, s, t):
    # Create a list of characters to use
    chars = ['a'] * n + ['b'] * n + ['c'] * n
    
    # Check if it's possible to create a valid string
    if s[0] == t[0] or s[0] == t[1] or s[1] == t[0] or s[1] == t[1]:
        print("NO")
        return
    
    # Create a result string
    res = []
    
    # Start with the first character that is not in s or t
    for i in range(n):
        if i % 3 == 0:
            res.append('a')
        elif i % 3 == 1:
            res.append('b')
        else:
            res.append('c')
    
    # Convert list to string
    res = ''.join(res)
    
    # Check for substrings and adjust if necessary
    for i in range(len(res) - 1):
        if res[i:i+2] == s or res[i:i+2] == t:
            # Swap the last character with the current one
            if i + 2 < len(res):
                res = res[:i] + res[i+1] + res[i] + res[i+2:]
            else:
                res = res[:i] + res[i+1] + res[i]
            break
    
    print("YES")
    print(res)

# Input reading
n = int(input())
s = input().strip()
t = input().strip()

generate_string(n, s, t)