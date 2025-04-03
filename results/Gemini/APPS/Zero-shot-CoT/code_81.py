def solve():
    n = int(input())
    strings = []
    for _ in range(n):
        strings.append(input())

    def is_substring(a, b):
        return a in b

    import itertools
    
    for perm in itertools.permutations(strings):
        valid = True
        for i in range(1, len(perm)):
            for j in range(i):
                if not is_substring(perm[j], perm[i]):
                    valid = False
                    break
            if not valid:
                break
        
        if valid:
            print("YES")
            for s in perm:
                print(s)
            return
    
    print("NO")

solve()