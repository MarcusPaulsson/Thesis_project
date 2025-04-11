def solve():
    n = int(input())
    strings = [input() for _ in range(n)]
    
    def is_substring(a, b):
        return a in b

    def check_order(order):
        for i in range(1, len(order)):
            for j in range(i):
                if not is_substring(order[j], order[i]):
                    return False
        return True

    import itertools
    
    for perm in itertools.permutations(strings):
        if check_order(list(perm)):
            print("YES")
            for s in perm:
                print(s)
            return
    
    print("NO")

solve()