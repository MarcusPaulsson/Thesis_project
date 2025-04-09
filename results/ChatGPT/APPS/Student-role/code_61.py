def max_possible_number(n, a, f):
    a = list(a)
    f = [0] + f  # to align f(1) to f(9) with indices 1 to 9
    modified = False
    
    for i in range(n):
        original_digit = int(a[i])
        new_digit = f[original_digit]
        
        if new_digit > original_digit:
            if not modified:
                modified = True
                # Start replacing until we find a digit that doesn't increase
            a[i] = str(new_digit)
        elif new_digit < original_digit and modified:
            # Once we start modifying, we should stop if we encounter a digit that doesn't increase
            break
    
    return ''.join(a)

# Input reading
n = int(input().strip())
a = input().strip()
f = list(map(int, input().strip().split()))

# Function call and output
result = max_possible_number(n, a, f)
print(result)