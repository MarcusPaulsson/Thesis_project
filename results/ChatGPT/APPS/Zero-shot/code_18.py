def lexicographically_minimal_string(s):
    t = []
    u = []
    
    for char in s:
        # Move character from s to t
        t.append(char)
        
        # While t is not empty and we can pop from t to u
        while t:
            # If u is empty or the last character in u is less than or equal to the last in t
            if not u or t[-1] >= u[-1]:
                break
            # Pop from t to u
            u.append(t.pop())
    
    # After processing all characters in s, pop remaining characters from t to u
    while t:
        u.append(t.pop())
    
    # Convert list u back to string and return
    return ''.join(u)

# Input
s = input().strip()
# Output the result
print(lexicographically_minimal_string(s))