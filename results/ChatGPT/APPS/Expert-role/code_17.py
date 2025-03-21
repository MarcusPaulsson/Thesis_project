def count_tuples(n, a):
    from collections import defaultdict
    
    # Count occurrences of each value in the array
    value_indices = defaultdict(list)
    for index, value in enumerate(a):
        value_indices[value].append(index + 1)  # Store 1-based index
    
    total_tuples = 0
    
    # For each number, calculate the number of valid tuples
    for indices in value_indices.values():
        m = len(indices)
        if m < 2:
            continue  # Need at least two indices for a valid pair
        
        # Calculate pairs of indices for (i, k)
        for j in range(1, n - 1):
            if a[j] in value_indices:
                for l in range(j + 1, n + 1):
                    if a[l - 1] == a[j]:
                        # Count valid (i, k) pairs
                        count_i_k = 0
                        for i in indices:
                            if i < j:
                                count_i_k += 1
                        total_tuples += count_i_k
    
    return total_tuples

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = count_tuples(n, a)
    print(result)