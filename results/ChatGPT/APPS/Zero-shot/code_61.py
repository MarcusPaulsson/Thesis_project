n = int(input())
a = input().strip()
f = list(map(int, input().strip().split()))

# Convert f to a mapping from characters
f_map = {str(i + 1): str(f[i]) for i in range(9)}

# Initialize result as the original number
result = a

# Flag to indicate if we are replacing the segment
replacing = False
new_number = []

for digit in a:
    if not replacing and f_map[digit] > digit:
        # Start replacing
        replacing = True
    elif replacing and f_map[digit] < digit:
        # Stop replacing if we see a digit that should not be replaced
        replacing = False
        
    if replacing:
        new_number.append(f_map[digit])
    else:
        new_number.append(digit)

# Join the new number and compare with original
max_number = ''.join(new_number)
print(max(max_number, a))