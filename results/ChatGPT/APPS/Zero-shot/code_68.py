def minimum_cost_to_obtain_set(n, k, s):
    # Count the number of unique subsequences of the string s
    unique_chars = set(s)
    unique_count = len(unique_chars)

    # Calculate the maximum number of unique subsequences
    max_unique_subsequences = (1 << unique_count) - 1  # 2^unique_count - 1
    if k > max_unique_subsequences:
        return -1

    # Generate all subsequences
    subsequences = set()
    for i in range(1 << n):
        subsequence = []
        for j in range(n):
            if i & (1 << j):
                subsequence.append(s[j])
        subsequences.add(''.join(subsequence))

    subsequences = list(subsequences)
    subsequences.sort(key=len)  # Sort by length

    total_cost = 0
    for i in range(k):
        if i < len(subsequences):
            total_cost += n - len(subsequences[i])
        else:
            return -1

    return total_cost

# Input handling
n, k = map(int, input().split())
s = input().strip()

# Calculate the result and print it
result = minimum_cost_to_obtain_set(n, k, s)
print(result)