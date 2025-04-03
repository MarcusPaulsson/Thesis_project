def min_cost_to_obtain_set(n, k, s):
    # Generate all unique subsequences using a set
    subsequences = set()
    
    # Function to generate subsequences using recursion
    def generate_subsequences(prefix, index):
        if index == n:
            if prefix:
                subsequences.add(prefix)
            return
        # Include current character
        generate_subsequences(prefix + s[index], index + 1)
        # Exclude current character
        generate_subsequences(prefix, index + 1)

    # Start generating subsequences from the first character
    generate_subsequences("", 0)
    
    # Check if we have enough unique subsequences
    if len(subsequences) < k:
        return -1
    
    # Calculate the total minimum cost
    # Sort subsequences by their lengths
    sorted_subsequences = sorted(subsequences, key=len)
    total_cost = 0
    for i in range(k):
        total_cost += n - len(sorted_subsequences[i])
    
    return total_cost

# Read input
n, k = map(int, input().split())
s = input().strip()

# Get the result and print it
result = min_cost_to_obtain_set(n, k, s)
print(result)