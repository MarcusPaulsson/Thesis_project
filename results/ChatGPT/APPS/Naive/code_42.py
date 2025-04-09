def count_cyclic_strings(n, s):
    from collections import defaultdict

    m = len(s)
    # Create all possible binary strings of length n
    total_strings = 2 ** n

    # Function to check if a string contains s as a substring
    def contains_substring(t):
        t_double = t + t  # To account for cyclic shifts
        return s in t_double

    # Count valid cyclic strings
    valid_count = 0
    for i in range(total_strings):
        t = bin(i)[2:].zfill(n)  # Get binary representation of length n
        if contains_substring(t):
            valid_count += 1

    return valid_count

# Input reading
n = int(input())
s = input().strip()

# Output the result
print(count_cyclic_strings(n, s))