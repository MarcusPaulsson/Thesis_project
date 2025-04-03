n = int(input())
a = list(map(int, input().split()))

total_sum = sum(a)
nice_indices = []

for i in range(n):
    remaining_sum = total_sum - a[i]
    if remaining_sum == a[i] * 2:  # Check if the remaining sum equals twice the removed element
        nice_indices.append(i + 1)  # Store the 1-based index

print(len(nice_indices))
if nice_indices:
    print(' '.join(map(str, nice_indices)))