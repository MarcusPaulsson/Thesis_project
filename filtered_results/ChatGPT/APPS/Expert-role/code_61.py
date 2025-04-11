def max_number_after_replacement(n, a, f):
    a_list = list(a)
    modified = False
    
    for i in range(n):
        original_digit = int(a_list[i])
        new_digit = f[original_digit - 1]
        
        if new_digit > original_digit and not modified:
            # Start modifying the segment
            modified = True
            a_list[i] = str(new_digit)
        elif new_digit >= original_digit and modified:
            # Continue modifying the segment
            a_list[i] = str(new_digit)
        elif new_digit < original_digit and modified:
            # Stop modifying the segment
            break
    
    return ''.join(a_list)

# Input reading
n = int(input())
a = input().strip()
f = list(map(int, input().strip().split()))

# Get the result and print
result = max_number_after_replacement(n, a, f)
print(result)