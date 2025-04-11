def restore_permutation(n, q):
    p = [0] * n
    p[0] = 0  # We can start from any arbitrary value, we will adjust later

    # Calculate p based on q
    for i in range(1, n):
        p[i] = p[i - 1] + q[i - 1]

    # Find the minimum value in p
    min_p = min(p)

    # Adjust p to make the smallest value 1
    adjustment = 1 - min_p
    for i in range(n):
        p[i] += adjustment

    # Check if p is a valid permutation
    if len(set(p)) == n and all(1 <= x <= n for x in p):
        print(" ".join(map(str, p)))
    else:
        print(-1)

# Input reading
n = int(input())
q = list(map(int, input().split()))

restore_permutation(n, q)