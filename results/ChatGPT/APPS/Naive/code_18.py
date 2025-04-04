def lexicographically_minimal(s):
    # Initialize strings t and u
    t = []
    u = []
    
    # Process characters in the input string
    for char in s:
        t.append(char)
        # Attempt to pop from t to u if possible
        while t and (not u or t[-1] <= u[-1]):
            u.append(t.pop())
    
    # If there are still characters in t, pop them to u
    while t:
        u.append(t.pop())
    
    # Join the list u into a string and return
    return ''.join(u)

# Read input
s = input().strip()
# Get the result and print it
result = lexicographically_minimal(s)
print(result)