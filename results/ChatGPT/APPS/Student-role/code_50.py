def min_jars_to_empty(t, test_cases):
    results = []
    for n, jars in test_cases:
        count1 = jars.count(1)
        count2 = jars.count(2)
        
        # If the counts are already equal, no jars need to be emptied
        if count1 == count2:
            results.append(0)
            continue
        
        # Calculate how many we need to remove to balance
        imbalance = abs(count1 - count2) // 2
        
        # We need to find the minimum number of jars to empty
        # The number of jars to empty is the total imbalance
        total_jars_to_empty = 0
        
        # We can keep removing from both sides to balance
        for i in range(2*n):
            if jars[i] == 1:
                count1 -= 1
            else:
                count2 -= 1
            
            total_jars_to_empty += 1
            
            if count1 == count2:
                break
        
        results.append(total_jars_to_empty)
    
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    jars = list(map(int, input().split()))
    test_cases.append((n, jars))

# Getting results
results = min_jars_to_empty(t, test_cases)

# Output results
for res in results:
    print(res)