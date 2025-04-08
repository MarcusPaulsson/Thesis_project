def max_after_replacement(n, a, f):
    # Create a mapping of original digits to their replacements
    f_map = {str(i + 1): str(f[i]) for i in range(9)}

    # Convert the input number into a list of characters for easy manipulation
    result = list(a)
    replacement_started = False

    for i in range(n):
        current_digit = a[i]
        new_digit = f_map[current_digit]

        # Start replacing if the new digit is greater than the current digit
        if new_digit > current_digit and not replacement_started:
            replacement_started = True
            result[i] = new_digit
        # Continue replacing as long as it is beneficial
        elif replacement_started:
            if new_digit >= current_digit:
                result[i] = new_digit
            else:
                break  # Stop if no further benefit

    return ''.join(result)

# Input reading
n = int(input().strip())
a = input().strip()
f = list(map(int, input().strip().split()))

# Output the result
print(max_after_replacement(n, a, f))