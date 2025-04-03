def min_tree_height(t, test_cases):
    results = []
    for case in test_cases:
        n, a = case
        height = 0
        current_level = [1]  # Start with the root
        index = 1  # Start from the second element, since first is the root

        while index < n:
            next_level = []
            for node in current_level:
                # While we can add children to the current node
                while index < n and a[index] > node:
                    next_level.append(a[index])
                    index += 1
            current_level = next_level
            height += 1
        
        results.append(height)
    
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    test_cases.append((n, a))

# Calculate and print results
results = min_tree_height(t, test_cases)
for res in results:
    print(res)