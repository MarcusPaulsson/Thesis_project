def solve():
    n, k = map(int, input().split())

    def decomposition(p):
        unmarked = [True] * n
        l = []
        for i in range(n):
            if unmarked[i]:
                reachable = []
                curr = i
                while unmarked[curr]:
                    reachable.append(curr)
                    unmarked[curr] = False
                    curr = p[curr] - 1
                
                max_val = -1
                max_idx = -1
                for j in range(len(reachable)):
                    if p[reachable[j]] > max_val:
                        max_val = p[reachable[j]]
                        max_idx = j
                
                shifted_reachable = reachable[max_idx:] + reachable[:max_idx]
                
                l.append([p[idx] for idx in shifted_reachable])
        return l

    def new_year_transformation(p):
        decomp = decomposition(p)
        decomp.sort(key=lambda x: x[0])
        result = []
        for sublist in decomp:
            result.extend(sublist)
        return result
    
    def is_good(p):
        return new_year_transformation(p) == p

    good_permutations = []
    
    import itertools
    
    all_permutations = list(itertools.permutations(range(1, n + 1)))
    
    for perm in all_permutations:
        p = list(perm)
        if is_good(p):
            good_permutations.append(p)
            
    good_permutations.sort()

    if k > len(good_permutations):
        print(-1)
    else:
        print(*good_permutations[k-1])

t = int(input())
for _ in range(t):
    solve()