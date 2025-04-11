a, b, x = map(int, input().split())

# Determine the starting character based on the number of 0s and 1s
if a > b:
    start = '0'
else:
    start = '1'

# Create the base pattern
pattern = []
for i in range(x + 1):
    if i % 2 == 0:
        pattern.append(start)
    else:
        pattern.append('1' if start == '0' else '0')

# Count how many 0s and 1s we have used
used_0s = pattern.count('0')
used_1s = pattern.count('1')

# Calculate remaining 0s and 1s
remaining_0s = a - used_0s
remaining_1s = b - used_1s

# Append remaining 0s and 1s to the pattern
if remaining_0s > 0:
    pattern.append('0' * remaining_0s)
if remaining_1s > 0:
    pattern.append('1' * remaining_1s)

# Join the pattern into a string
result = ''.join(pattern)

# Print the result
print(result)