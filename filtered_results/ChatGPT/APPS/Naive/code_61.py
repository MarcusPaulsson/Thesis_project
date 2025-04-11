def max_number_after_replacement(n, a, f):
    a_list = list(a)
    modified = False

    for i in range(n):
        original_digit = int(a_list[i])
        new_digit = f[original_digit - 1]
        
        if new_digit > original_digit:
            a_list[i] = str(new_digit)
            modified = True
        elif modified and new_digit < original_digit:
            break

    return ''.join(a_list)

# Input reading
n = int(input().strip())
a = input().strip()
f = list(map(int, input().strip().split()))

# Get the result and print
result = max_number_after_replacement(n, a, f)
print(result)