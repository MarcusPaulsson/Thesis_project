def solve():
    n = int(input())
    s = input()
    t = input()

    def check(res, s, t):
        for i in range(len(res) - 1):
            sub = res[i:i+2]
            if sub == s or sub == t:
                return False
        return True

    import itertools
    
    chars = ['a'] * n + ['b'] * n + ['c'] * n
    
    for p in itertools.permutations(chars):
        res = "".join(p)
        if check(res, s, t):
            print("YES")
            print(res)
            return

    print("NO")

solve()