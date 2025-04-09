n = int(input())
a = list(map(int, input().split()))

total_sum = sum(a)
nice_indices = []

for i in range(n):
    removed_element = a[i]
    remaining_sum = total_sum - removed_element
    
    if remaining_sum % 2 == 0:
        target = remaining_sum // 2
        # Check if target is in the remaining array
        if (target == removed_element and a.count(target) > 1) or (target != removed_element and target in a):
            nice_indices.append(i + 1)

print(len(nice_indices))
if nice_indices:
    print(" ".join(map(str, nice_indices)))