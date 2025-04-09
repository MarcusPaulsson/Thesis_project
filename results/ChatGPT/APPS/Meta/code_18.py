def lexicographically_minimal_string(s):
    t = []  # Stack to hold characters from s
    u = []  # Result string
    index = 0  # Pointer for s

    while index < len(s) or t:
        # Move characters from s to t
        while index < len(s):
            t.append(s[index])
            index += 1
            
            # Check if we can pop from t to u
            while t and (not u or u[-1] <= t[-1]):
                u.append(t.pop())

        # If t is not empty, we can still pop from it to u
        while t:
            u.append(t.pop())

    return ''.join(u)

# Read input
s = input().strip()
# Get the result
result = lexicographically_minimal_string(s)
# Print result
print(result)