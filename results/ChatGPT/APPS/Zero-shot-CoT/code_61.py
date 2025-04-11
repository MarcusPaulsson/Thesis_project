n = int(input())
a = input().strip()
f = list(map(int, input().strip().split()))

# Convert f to a list where f[i] corresponds to f(i+1)
f = [0] + f  # Adding a dummy value at index 0 for convenience

max_number = a  # Start with the original number as the maximum

# We will try to find the best segment to replace
i = 0
while i < n:
    # Start of a potential segment
    start = i
    while i < n and f[int(a[i])] >= int(a[i]):
        i += 1
    # Now i is at the first position where we can't replace or at the end
    if start < i:  # We found a segment to replace
        # Create a new number with this segment replaced
        new_number = a[:start] + ''.join(str(f[int(a[j])]) for j in range(start, i)) + a[i:]
        max_number = max(max_number, new_number)
    i += 1  # Move to the next character

print(max_number)