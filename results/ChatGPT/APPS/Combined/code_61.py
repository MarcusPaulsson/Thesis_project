def max_after_replacement(n, a, f):
    a_list = list(a)
    f = [0] + f  # Adjust index to match digit values (1-9)
    
    modified = False
    for i in range(n):
        original_digit = int(a_list[i])
        new_digit = f[original_digit]
        
        if new_digit > original_digit and not modified:
            modified = True
        
        if modified:
            a_list[i] = str(new_digit)
        
        if modified and new_digit < original_digit:
            break
    
    return ''.join(a_list)

# Input reading
n = int(input())
a = input().strip()
f = list(map(int, input().strip().split()))

# Output the result
print(max_after_replacement(n, a, f))