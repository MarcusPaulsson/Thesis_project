def alice_score(test_cases):
    results = []
    for s in test_cases:
        alice_score = 0
        current_count = 0
        
        for char in s:
            if char == '1':
                current_count += 1
            else:
                alice_score += (current_count + 1) // 2  # Alice takes the odd counts
                current_count = 0
        
        alice_score += (current_count + 1) // 2  # Add the last segment if it ends with '1'
        results.append(alice_score)
    
    return results

# Read input
T = int(input())
test_cases = [input().strip() for _ in range(T)]

# Get results
results = alice_score(test_cases)

# Print results
for result in results:
    print(result)