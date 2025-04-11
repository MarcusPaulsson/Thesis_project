n = int(input())
a = input().strip()
f = list(map(int, input().strip().split()))

# Convert f to a string for easier manipulation
f_str = ''.join(map(str, f))

# Initialize the maximum number as the original number
max_number = a

# Flag to indicate if we are in a segment that we are replacing
in_segment = False
new_number = []

for i in range(n):
    original_digit = a[i]
    mapped_digit = f_str[int(original_digit) - 1]
    
    if mapped_digit > original_digit:
        # Start replacing if we haven't started a segment yet
        if not in_segment:
            in_segment = True
            new_number.append(mapped_digit)
        else:
            new_number.append(mapped_digit)
    elif mapped_digit < original_digit:
        # If we hit a digit that doesn't improve, we stop the segment
        if in_segment:
            in_segment = False
        new_number.append(original_digit)
    else:
        # If they are equal, just append the original
        new_number.append(original_digit)

# Join the new number list into a string
new_number_str = ''.join(new_number)

# Compare with the original number and print the maximum
print(max(max_number, new_number_str))