def solve():
    n, k = map(int, input().split())

    def get_decomposition(p):
        n = len(p)
        marked = [False] * n
        decomposition = []

        for i in range(n):
            if not marked[i]:
                reachable = []
                curr = i
                while not marked[curr]:
                    reachable.append(p[curr])
                    marked[curr] = True
                    curr = p[curr] - 1
                
                max_val = max(reachable)
                max_index = reachable.index(max_val)
                
                shifted_reachable = reachable[max_index:] + reachable[:max_index]
                decomposition.append(shifted_reachable)
        
        return decomposition

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
        permutations = []
        for p in itertools.permutations(range(1, n + 1)):
            permutations.append(list(p))
        return permutations
    
    good_permutations = []
    for p in generate_permutations(n):
        if is_good(p):
            good_permutations.append(p)
    
    good_permutations.sort()

    if len(good_permutations) < k:
        print("-1")
    else:
        print(*good_permutations[k - 1])

t = int(input())
for _ in range(t):
    solve()