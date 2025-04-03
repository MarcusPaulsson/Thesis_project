def good_permutations(n):
    if n == 1:
        return [[1]]
    
    perms = []
    for perm in good_permutations(n - 1):
        for i in range(n):
            new_perm = perm[:i] + [n] + perm[i:]
            perms.append(new_perm)
    
    return perms

def count_good_permutations(n):
    return len(good_permutations(n))

def find_kth_good_permutation(n, k):
    good_perms = good_permutations(n)
    if k > len(good_perms):
        return -1
    return good_perms[k - 1]

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    result = find_kth_good_permutation(n, k)
    if result == -1:
        print(-1)
    else:
        print(' '.join(map(str, result)))