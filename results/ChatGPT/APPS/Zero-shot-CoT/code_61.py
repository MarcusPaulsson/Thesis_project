n = int(input().strip())
a = input().strip()
f = list(map(int, input().strip().split()))

# Convert digits in a to their mapped values using f
mapped_a = [str(f[int(d) - 1]) for d in a]

# Initialize the result as the original number
result = a

# Find maximum by trying to replace segments
for i in range(n):
    # Start replacing from index i
    current = list(a)
    for j in range(i, n):
        # Replace current digit with its mapped value
        current[j] = str(f[int(a[j]) - 1])
        # Create the new number after replacement
        new_number = ''.join(current)
        # Update the result if the new number is greater
        if new_number > result:
            result = new_number

print(result)