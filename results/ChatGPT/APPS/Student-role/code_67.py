def can_make_equal(k, test_cases):
    results = []
    
    for case in range(k):
        n = test_cases[case][0]
        s = list(test_cases[case][1])
        t = list(test_cases[case][2])
        
        # Count character occurrences
        from collections import Counter
        count_s = Counter(s)
        count_t = Counter(t)
        
        # Combine counts
        combined_counts = count_s + count_t
        
        # Check if the combined counts have even occurrences for each character
        can_equal = all(count % 2 == 0 for count in combined_counts.values())
        
        if not can_equal:
            results.append("No")
            continue
        
        results.append("Yes")
        operations = []
        
        # Make a list of mismatched positions
        mismatched_s = []
        mismatched_t = []
        
        for i in range(n):
            if s[i] != t[i]:
                mismatched_s.append(i)
                mismatched_t.append(i)
        
        # Now we need to swap characters to make them equal
        for i in range(len(mismatched_s)):
            if s[mismatched_s[i]] == t[mismatched_t[i]]:
                continue
            
            # Find the character in t that needs to come to s
            target_char = s[mismatched_s[i]]
            target_index_in_t = -1
            
            for j in range(n):
                if t[j] == target_char and j not in mismatched_t:
                    target_index_in_t = j
                    break
            
            if target_index_in_t != -1:
                # Swap to bring the correct character into position
                operations.append((mismatched_s[i] + 1, target_index_in_t + 1))  # 1-indexed
                s[mismatched_s[i]], t[target_index_in_t] = t[target_index_in_t], s[mismatched_s[i]]
            
            # After this, we should have a match at mismatched_s[i]
            if s[mismatched_s[i]] != t[mismatched_s[i]]:
                # If not matched, we need an extra swap to fix it
                operations.append((mismatched_s[i] + 1, mismatched_s[i] + 1))
                operations.append((mismatched_s[i] + 1, mismatched_t[i] + 1))
        
        results.append(f"{len(operations)}")
        for op in operations:
            results.append(f"{op[0]} {op[1]}")
    
    return results

# Read input
k = int(input())
test_cases = []
for _ in range(k):
    n = int(input())
    s = input().strip()
    t = input().strip()
    test_cases.append((n, s, t))

# Get results
results = can_make_equal(k, test_cases)

# Print results
for res in results:
    print(res)