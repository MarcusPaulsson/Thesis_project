def restore_permutation(n, k, p):
    if k == 1:
        return p + list(range(n, 1, -1))
    if p[k-1] > p[k-2]:
        return p + list(range(n, k, -1)) + [k-1]
    else:
        return -1

n, k = map(int, input().split())
p = list(map(int, input().split()))
print(restore_permutation(n, k, p))