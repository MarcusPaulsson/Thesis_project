def find_permutations(t, test_cases):
    results = []
    
    for case in test_cases:
        n, a = case
        count = {}
        
        # Count occurrences of each number
        for num in a:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Find valid (l1, l2) pairs
        valid_pairs = []
        prefix_set = set()
        suffix_set = set()
        
        for i in range(n):
            # Update prefix and suffix
            prefix_set.add(a[i])
            suffix_set.clear()
            for j in range(i + 1, n):
                suffix_set.add(a[j])
            
            l1, l2 = i + 1, n - (i + 1)
            if (len(prefix_set) == l1) and (len(suffix_set) == l2):
                valid_pairs.append((l1, l2))
        
        results.append(valid_pairs)
    
    output = []
    for valid_pairs in results:
        output.append(str(len(valid_pairs)))
        for l1, l2 in valid_pairs:
            output.append(f"{l1} {l2}")
    
    print("\n".join(output))

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Function call
find_permutations(t, test_cases)