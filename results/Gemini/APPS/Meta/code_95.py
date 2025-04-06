def solve():
    n = int(input())
    s = input()
    t = input()

    chars = ['a', 'b', 'c']

    import itertools
    for perm in itertools.permutations(chars):
        res = ""
        
        
        res1 = ""
        for _ in range(n):
            res1 += perm[0]
        for _ in range(n):
            res1 += perm[1]
        for _ in range(n):
            res1 += perm[2]

        
        is_valid1 = True
        if s in res1 or t in res1:
            is_valid1 = False
            
            
        if is_valid1:
            print("YES")
            print(res1)
            return

        res2 = ""

        for _ in range(n):
            res2 += perm[0]
        for _ in range(n):
            res2 += perm[2]
        for _ in range(n):
            res2 += perm[1]
            
        is_valid2 = True
        if s in res2 or t in res2:
            is_valid2 = False
            
        if is_valid2:
            print("YES")
            print(res2)
            return
            
    print("NO")

solve()