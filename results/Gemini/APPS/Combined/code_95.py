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

    chars = ['a', 'b', 'c']

    import itertools

    for perm in itertools.permutations(chars):
        res = ""
        res += perm[0] * n
        res += perm[1] * n
        res += perm[2] * n

        if check(res, s, t):
            print("YES")
            print(res)
            return
    
    for perm in itertools.permutations(chars):
        res = ""
        res += perm[2] * n
        res += perm[1] * n
        res += perm[0] * n

        if check(res, s, t):
            print("YES")
            print(res)
            return

    print("NO")

solve()