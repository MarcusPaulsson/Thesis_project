def solve():
    n = int(input())
    s = input()
    t = input()

    def check(res, s, t):
        for i in range(len(res) - 1):
            if res[i:i+2] == s or res[i:i+2] == t:
                return False
        return True

    import itertools
    
    chars = ['a'] * n + ['b'] * n + ['c'] * n
    
    for perm in itertools.permutations(chars):
        res = "".join(perm)
        if check(res, s, t):
            print("YES")
            print(res)
            return
    
    print("NO")

solve()