n, k = map(int, input().split())
s = input().strip()

# Step 1: Find unique characters and their counts
from collections import Counter

counter = Counter(s)
unique_chars = list(counter.keys())
unique_count = len(unique_chars)

# Step 2: Calculate the maximum number of unique subsequences
max_unique_subsequences = 0
cost = 0

# We will add all subsequences of unique characters
for i in range(1, unique_count + 1):
    max_unique_subsequences += i  # The number of subsequences of length i is `C(unique_count, i) * 2^i`

# Step 3: Check if we can create at least k unique subsequences
if max_unique_subsequences < k:
    print(-1)
else:
    # Calculate the minimum total cost
    total_cost = 0
    subsequence_count = 0
    
    # We calculate cost for each unique character
    for char in unique_chars:
        count = counter[char]
        for i in range(1, count + 1):
            if subsequence_count < k:
                total_cost += (n - (1 + i - 1))  # Add subsequence with length i
                subsequence_count += 1
            else:
                break
        if subsequence_count >= k:
            break
    
    # If we still need more subsequences, we need to use duplicates
    if subsequence_count < k:
        needed = k - subsequence_count
        total_cost += needed * n  # Adding duplicates of full length costs `n` each time
    
    print(total_cost)