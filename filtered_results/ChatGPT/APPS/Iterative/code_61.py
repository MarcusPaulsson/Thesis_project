n = int(input())
a = input().strip()
f = list(map(int, input().strip().split()))

max_number = a  # Start with the original number as the maximum

# We will check for the best segment to replace
i = 0
while i < n:
    # If the current digit can be improved
    if f[int(a[i]) - 1] > int(a[i]):
        # Start a segment to replace
        start = i
        while i < n and f[int(a[i]) - 1] >= int(a[i]):
            i += 1
        # Create the new number with the segment replaced
        new_number = a[:start] + ''.join(str(f[int(a[j]) - 1]) for j in range(start, i)) + a[i:]
        max_number = max(max_number, new_number)
    else:
        i += 1

print(max_number)