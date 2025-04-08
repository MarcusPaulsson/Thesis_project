def lexicographically_minimal_string(s):
    t = []
    u = []
    
    s_list = list(s)
    
    while s_list or t:
        if s_list:
            t.append(s_list.pop(0))
        
        while t:
            if not s_list or t[-1] <= s_list[0]:
                u.append(t.pop())
            else:
                break
    
    return ''.join(u)

# Read input
s = input().strip()
# Print the result
print(lexicographically_minimal_string(s))