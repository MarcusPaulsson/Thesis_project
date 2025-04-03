def minimum_tree_height(test_cases):
    results = []
    
    for n, a in test_cases:
        depth = 0
        current_level = 1
        nodes_at_current_level = 1
        
        for i in range(1, n):
            if a[i] < a[i - 1]:
                depth += 1
                current_level = 1
                nodes_at_current_level = 1
            else:
                nodes_at_current_level += 1
            
            if nodes_at_current_level > current_level:
                current_level = nodes_at_current_level
        
        results.append(depth + 1)
    
    return results

# Reading input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Getting results
results = minimum_tree_height(test_cases)

# Printing output
for res in results:
    print(res)