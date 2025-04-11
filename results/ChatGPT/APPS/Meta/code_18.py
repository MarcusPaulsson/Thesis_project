def lexicographically_minimal_string(s):
    t = []
    u = []
    
    for char in s:
        # Append the character from s to t
        t.append(char)
        
        # While t is not empty and the last character of t is the smallest possible
        while t:
            # Find the smallest character in t
            min_char = min(t)
            # If the last character of t is the smallest, pop it to u
            if t[-1] == min_char:
                u.append(t.pop())
            else:
                break
    
    # Join the list u to form the resulting string
    return ''.join(u)

# Input reading
s = input().strip()
# Output the result
print(lexicographically_minimal_string(s))