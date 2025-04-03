def solve():
    n, k = map(int, input().split())

    def get_decomposition(p):
        marked = [False] * n
        l = []
        for i in range(n):
            if not marked[i]:
                reachable = []
                curr = i
                while not marked[curr]:
                    reachable.append(curr)
                    marked[curr] = True
                    curr = p[curr] - 1
                
                max_val = 0
                max_idx = -1
                for j in range(len(reachable)):
                    if p[reachable[j]] > max_val:
                        max_val = p[reachable[j]]
                        max_idx = j
                
                shifted_reachable = reachable[max_idx:] + reachable[:max_idx]
                
                l.append([p[x] for x in shifted_reachable])
        return l
    
    def new_year_transformation(p):
        decomposition = get_decomposition(p)
        decomposition.sort(key=lambda x: x[0])
        
        result = []
        for sublist in decomposition:
            result.extend(sublist)
        return result
    
    def is_good(p):
        return new_year_transformation(p) == p
    
    def generate_permutations(n):
        import itertools
        perms = []
        for p in itertools.permutations(range(1, n + 1)):
            perms.append(list(p))
        return perms
    
    good_permutations = []
    for p in generate_permutations(n):
        if is_good(p):
            good_permutations.append(p)
    
    good_permutations.sort()
    
    if len(good_permutations) < k:
        print(-1)
    else:
        print(*good_permutations[k - 1])


t = int(input())
for _ in range(t):
    solve()