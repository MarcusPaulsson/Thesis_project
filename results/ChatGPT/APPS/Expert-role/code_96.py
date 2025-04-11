def restore_permutation(n, q):
    p = [0] * n
    p[0] = 0  # We can start from any arbitrary number, we will adjust later

    for i in range(1, n):
        p[i] = p[i - 1] + q[i - 1]

    min_p = min(p)
    # Shift the permutation to make the smallest element 1
    shift = 1 - min_p

    for i in range(n):
        p[i] += shift

    # Check if the resulting permutation is valid
    if len(set(p)) == n and all(1 <= x <= n for x in p):
        print(" ".join(map(str, p)))
    else:
        print(-1)

# Example usage:
n = int(input())
q = list(map(int, input().split()))
restore_permutation(n, q)