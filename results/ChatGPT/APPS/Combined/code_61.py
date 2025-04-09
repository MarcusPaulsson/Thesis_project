def maximize_number(n, a, f):
    f_map = {str(i + 1): str(f[i]) for i in range(9)}
    result = list(a)
    
    in_replacement_segment = False
    
    for i in range(n):
        current_digit = a[i]
        mapped_digit = f_map[current_digit]
        
        if mapped_digit > current_digit:
            result[i] = mapped_digit
            in_replacement_segment = True
        elif mapped_digit < current_digit and in_replacement_segment:
            break
    
    return ''.join(result)

# Read inputs
n = int(input().strip())
a = input().strip()
f = list(map(int, input().strip().split()))

# Get the result
print(maximize_number(n, a, f))