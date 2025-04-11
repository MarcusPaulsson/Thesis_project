def min_cost_to_obtain_set(n, k, s):
    # Step 1: Create a set to store unique subsequences
    unique_subsequences = set()
    
    # Step 2: Generate all possible subsequences
    for i in range(1 << n):  # There are 2^n possible subsequences
        subsequence = ''.join(s[j] for j in range(n) if i & (1 << j))
        unique_subsequences.add(subsequence)
    
    # Step 3: Calculate the cost for each unique subsequence
    costs = [n - len(subseq) for subseq in unique_subsequences]
    
    # Step 4: Sort costs to find the minimum total cost for k unique subsequences
    costs.sort()
    
    # Step 5: Check if we can obtain k unique subsequences
    if len(costs) < k:
        return -1
    
    # Step 6: Calculate the total minimum cost for the first k costs
    return sum(costs[:k])

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))