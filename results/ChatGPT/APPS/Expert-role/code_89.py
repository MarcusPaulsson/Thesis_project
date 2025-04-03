def min_tree_height(t, test_cases):
    results = []
    for n, a in test_cases:
        # Create a list to track the depth of each node
        depth = [0] * (n + 1)
        # Initialize the current depth level
        current_depth = 0
        
        # A queue to simulate BFS levels
        queue = []
        queue.append(1)  # Start with the root

        index = 1  # Start from the second element in the BFS order
        
        while queue:
            next_queue = []
            # Process all nodes at the current depth
            for node in queue:
                # Determine the children of the current node
                while index < n and a[index] > node:
                    next_queue.append(a[index])
                    depth[a[index]] = current_depth + 1
                    index += 1
            
            # Move to the next depth level
            queue = next_queue
            current_depth += 1
        
        # The maximum depth found will be the answer for this test case
        results.append(current_depth)

    return results

# Input reading
t = int(input().strip())
test_cases = []
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    test_cases.append((n, a))

# Get results
results = min_tree_height(t, test_cases)

# Output results
for result in results:
    print(result)