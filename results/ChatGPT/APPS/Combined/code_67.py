def find_nice_indices(n, a):
    total_sum = sum(a)
    count = {}
    
    # Count occurrences of each number
    for num in a:
        count[num] = count.get(num, 0) + 1

    nice_indices = []

    for i in range(n):
        # Calculate the remaining sum after removing a[i]
        remaining_sum = total_sum - a[i]

        # Check if there exists an element equal to the remaining sum divided by 2
        if remaining_sum % 2 == 0:
            target = remaining_sum // 2
            
            # Check if the target can be found in the array
            if target in count:
                # Ensure the middle element can be counted correctly
                if (target != a[i] and count[target] > 0) or (target == a[i] and count[target] > 1):
                    nice_indices.append(i + 1)  # Store 1-based index

    return nice_indices

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Finding nice indices
nice_indices = find_nice_indices(n, a)

# Output results
print(len(nice_indices))
if nice_indices:
    print(" ".join(map(str, nice_indices)))