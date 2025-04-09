def max_transformed_number(n, a, f):
    a_list = list(a)
    transformed = False

    for i in range(n):
        original_digit = int(a_list[i])
        new_digit = f[original_digit - 1]
        
        if new_digit > original_digit and not transformed:
            # Start transforming
            transformed = True
            a_list[i] = str(new_digit)
        elif new_digit < original_digit and transformed:
            # Stop transforming if we encounter a digit that would not increase the number
            break
        elif transformed:
            # Continue transforming
            a_list[i] = str(new_digit)

    return ''.join(a_list)

# Input reading
n = int(input().strip())
a = input().strip()
f = list(map(int, input().strip().split()))

# Get the result and print it
result = max_transformed_number(n, a, f)
print(result)