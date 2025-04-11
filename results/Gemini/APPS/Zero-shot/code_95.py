def solve():
    n = int(input())
    s = input()
    t = input()

    chars = ['a', 'b', 'c']

    import itertools

    for perm in itertools.permutations(chars):
        res = ""
        for _ in range(n):
            res += perm[0]
            res += perm[1]
            res += perm[2]

        valid = True
        for i in range(len(res) - 1):
            sub = res[i:i+2]
            if sub == s or sub == t:
                valid = False
                break
        
        if valid:
            print("YES")
            print(res)
            return

    print("NO")

solve()