def max_number_after_replacement(n, a, f):
    a_list = list(a)
    f = [0] + f  # Make f 1-indexed
    modified = False

    for i in range(n):
        current_digit = int(a_list[i])
        if f[current_digit] > current_digit:
            a_list[i] = str(f[current_digit])
            modified = True
        elif modified and f[current_digit] < current_digit:
            break  # Stop replacing once we encounter a digit that won't increase the number

    return ''.join(a_list)

# Reading input
n = int(input().strip())
a = input().strip()
f = list(map(int, input().strip().split()))

# Output the result
print(max_number_after_replacement(n, a, f))