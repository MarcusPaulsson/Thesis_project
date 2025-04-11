def lexicographically_minimal_string(s):
    t = []
    u = []
    n = len(s)
    index = 0

    while index < n or t:
        if index < n:
            t.append(s[index])
            index += 1
        
        # Move characters from t to u if possible
        while t:
            # Check if we can pop from t to u
            if not u or t[-1] <= u[-1]:
                u.append(t.pop())
            else:
                break

    return ''.join(u)

# Read input
s = input().strip()
# Get the result
result = lexicographically_minimal_string(s)
# Print the result
print(result)