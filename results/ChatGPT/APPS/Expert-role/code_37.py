def good_permutations(n):
    if n == 1:
        return [[1]]
    
    perms = []
    for i in range(1, n + 1):
        for p in good_permutations(n - 1):
            if i not in p:
                perms.append([i] + p)
    
    # Filter only good permutations
    good_perms = []
    for perm in perms:
        # Check if permutation is good
        decomposition = []
        marked = [False] * n
        for j in range(n):
            if not marked[perm[j] - 1]:
                cur_list = []
                idx = j
                while not marked[perm[idx] - 1]:
                    cur_list.append(perm[idx])
                    marked[perm[idx] - 1] = True
                    idx = perm[idx] - 1  # jump to the next index
                if cur_list:
                    max_idx = cur_list.index(max(cur_list))
                    cur_list = cur_list[max_idx:] + cur_list[:max_idx]  # cyclic shift
                    decomposition.append(cur_list)
        if decomposition:
            decomposition.sort(key=lambda x: x[0])
            flat_list = [item for sublist in decomposition for item in sublist]
            if flat_list == perm:
                good_perms.append(perm)
    
    return good_perms

from itertools import permutations

def k_th_good_permutation(n, k):
    good_perms = good_permutations(n)
    if len(good_perms) < k:
        return -1
    else:
        return good_perms[k - 1]

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    result = k_th_good_permutation(n, k)
    if result == -1:
        print(-1)
    else:
        print(' '.join(map(str, result)))