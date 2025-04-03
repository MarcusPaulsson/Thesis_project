def min_tree_height(t, test_cases):
    results = []
    for case in test_cases:
        n, a = case
        level = {}
        max_height = 0

        # The root is at level 0
        level[a[0]] = 0
        
        for i in range(1, n):
            current = a[i]
            # The parent should be the first vertex in `a` that is at the highest level less than the current
            parent_level = -1
            
            for j in range(i - 1, -1, -1):
                if level.get(a[j], -1) != -1:
                    parent_level = level[a[j]]
                    break
            
            # The current node's level is one more than the parent's level
            if parent_level != -1:
                level[current] = parent_level + 1
                max_height = max(max_height, level[current])
        
        results.append(max_height)

    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get results
results = min_tree_height(t, test_cases)

# Output
for result in results:
    print(result)