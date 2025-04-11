n = int(input())
a = input().strip()
f = list(map(int, input().split()))

# Convert f to a string for easier manipulation
f = [str(x) for x in f]

# Initialize the result as the original number
max_number = a

# Flag to indicate if we are in a replacement segment
in_segment = False
new_number = []

for digit in a:
    original_digit = digit
    mapped_digit = f[int(digit) - 1]
    
    if not in_segment and mapped_digit > original_digit:
        # Start a new segment
        in_segment = True
    
    if in_segment:
        # Replace the digit
        new_number.append(mapped_digit)
    else:
        # Keep the original digit
        new_number.append(original_digit)
    
    if in_segment and mapped_digit < original_digit:
        # End the segment if we find a digit that should not be replaced
        in_segment = False

# Join the new number and compare with the max_number
new_number_str = ''.join(new_number)
max_number = max(max_number, new_number_str)

print(max_number)