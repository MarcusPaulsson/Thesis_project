def restore_permutation(n, q):
    # Initialize the permutation array
    p = [0] * n
    # Start with p[0] as an unknown, we will calculate it later
    sum_q = 0
    
    # Calculate p[i] based on the differences in q
    for i in range(1, n):
        sum_q += q[i - 1]
        p[i] = sum_q
    
    # Now, we need to find a suitable p[0]
    min_p = min(p)
    # p[0] should be 1 - min_p to ensure the smallest number is 1
    p[0] = 1 - min_p
    
    # Generate the full permutation
    for i in range(1, n):
        p[i] += p[0]
    
    # Check if the generated permutation is valid
    if len(set(p)) == n and all(1 <= num <= n for num in p):
        print(' '.join(map(str, p)))
    else:
        print(-1)

# Read inputs
n = int(input())
q = list(map(int, input().split()))

# Call the function
restore_permutation(n, q)