def min_cost_to_obtain_set(n, k, s):
    # Step 1: Create a set to store unique subsequences
    unique_subsequences = set()
    
    # Step 2: Generate all possible subsequences
    for i in range(1 << n):  # There are 2^n possible subsequences
        subsequence = []
        for j in range(n):
            if i & (1 << j):  # Check if j-th bit is set
                subsequence.append(s[j])
        unique_subsequences.add(''.join(subsequence))
    
    # Step 3: Check if we can obtain k unique subsequences
    if len(unique_subsequences) < k:
        return -1
    
    # Step 4: Calculate the minimum cost
    sorted_subsequences = sorted(unique_subsequences, key=len)  # Sort by length
    total_cost = 0
    for i in range(k):
        total_cost += n - len(sorted_subsequences[i])  # Cost is n - |t|
    
    return total_cost

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))