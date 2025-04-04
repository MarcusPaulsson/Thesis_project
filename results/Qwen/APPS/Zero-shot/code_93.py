def construct_tree(n, d, k):
    if d > n - 1 or k < 2:
        return "NO"
    if d == n - 1:
        if k >= 3:
            return "YES\n" + "\n".join(f"{i} {i+1}" for i in range(1, n))
        else:
            return "NO"
    if d == 1:
        if k >= n - 1:
            return "YES\n" + "\n".join(f"{1} {i}" for i in range(2, n+1))
        else:
            return "NO"
    if d % 2 == 0:
        if k >= 3:
            return "YES\n" + "\n".join(f"{i} {i+1}" for i in range(1, n-d+1)) + "\n" + "\n".join(f"{n-d+1} {i}" for i in range(n-d+2, n+1)) + "\n" + "\n".join(f"{n-d+1} {i}" for i in range(2, n-d+2))
        else:
            return "NO"
    else:
        if k >= 3:
            return "YES\n" + "\n".join(f"{i} {i+1}" for i in range(1, n-d)) + "\n" + "\n".join(f"{n-d} {i}" for i in range(n-d+2, n+1)) + "\n" + "\n".join(f"{n-d} {i}" for i in range(2, n-d+2)) + "\n" + f"{n-d} {n-d+1}"
        else:
            return "NO"

n, d, k = map(int, input().split())
print(construct_tree(n, d, k))