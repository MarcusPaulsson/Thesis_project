def minimal_string(s):
    t = []
    u = []
    
    # Reverse iterate through the string s and build the t
    for char in s:
        t.append(char)
    
    # We will use a list to simulate the stack behavior for t
    t = t[::-1]  # Reverse t to treat it like a stack (LIFO)
    
    # While t is not empty, we will choose characters for u
    while t:
        # Find the minimum character from the current perspective in t
        min_char = min(t)
        min_index = t.index(min_char)
        
        # Append characters to u until we reach the min_index
        for _ in range(min_index + 1):
            u.append(t.pop(0))  # Pop from the front (simulating extraction from t)
        
        # Remove this character from t after adding to u
        if min_char in t:
            t.remove(min_char)
    
    # Join the list u to form the result string
    return ''.join(u)

# Read input
s = input().strip()
# Get the result and print
result = minimal_string(s)
print(result)