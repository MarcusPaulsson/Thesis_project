n = int(input())
a = input().strip()
f = list(map(int, input().strip().split()))

# Convert f to a dictionary for easier access
f_dict = {str(i + 1): str(f[i]) for i in range(9)}

# Initialize the result as the original number
max_number = a

# We will track if we have started replacing
started_replacing = False
new_segment = []

for digit in a:
    if not started_replacing and f_dict[digit] > digit:
        # Start replacing if we find a digit that can be increased
        started_replacing = True
        new_segment.append(f_dict[digit])
    elif started_replacing:
        if f_dict[digit] >= digit:
            # Continue replacing if we can keep the number the same or increase it
            new_segment.append(f_dict[digit])
        else:
            # Stop replacing if we find a digit that cannot be increased
            break
    else:
        # If we haven't started replacing, keep the original digit
        new_segment.append(digit)

# If we started replacing, we need to construct the new number
if started_replacing:
    # Join the new segment and append the rest of the original number
    new_number = ''.join(new_segment) + a[len(new_segment):]
    max_number = max(max_number, new_number)

print(max_number)