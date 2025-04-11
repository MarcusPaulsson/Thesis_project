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

    
    res1 = "a"*n + "b"*n + "c"*n
    res2 = "a"*n + "c"*n + "b"*n
    res3 = "b"*n + "a"*n + "c"*n
    res4 = "b"*n + "c"*n + "a"*n
    res5 = "c"*n + "a"*n + "b"*n
    res6 = "c"*n + "b"*n + "a"*n

    res1_rev = "c"*n + "b"*n + "a"*n
    res2_rev = "b"*n + "c"*n + "a"*n
    res3_rev = "c"*n + "a"*n + "b"*n
    res4_rev = "a"*n + "c"*n + "b"*n
    res5_rev = "b"*n + "a"*n + "c"*n
    res6_rev = "a"*n + "b"*n + "c"*n
    
    if check(res1, s, t):
        print("YES")
        print(res1)
        return
    if check(res2, s, t):
        print("YES")
        print(res2)
        return
    if check(res3, s, t):
        print("YES")
        print(res3)
        return
    if check(res4, s, t):
        print("YES")
        print(res4)
        return
    if check(res5, s, t):
        print("YES")
        print(res5)
        return
    if check(res6, s, t):
        print("YES")
        print(res6)
        return
    
    if check(res1_rev, s, t):
        print("YES")
        print(res1_rev)
        return
    if check(res2_rev, s, t):
        print("YES")
        print(res2_rev)
        return
    if check(res3_rev, s, t):
        print("YES")
        print(res3_rev)
        return
    if check(res4_rev, s, t):
        print("YES")
        print(res4_rev)
        return
    if check(res5_rev, s, t):
        print("YES")
        print(res5_rev)
        return
    if check(res6_rev, s, t):
        print("YES")
        print(res6_rev)
        return

    if s[0] != s[1] and t[0] != t[1]:
        res = "a" + "c" * n + "b" * n + "a" * (n - 1)
        if check(res, s, t):
            print("YES")
            print(res)
            return
        res = "b" + "a" * n + "c" * n + "b" * (n - 1)
        if check(res, s, t):
            print("YES")
            print(res)
            return
        res = "c" + "b" * n + "a" * n + "c" * (n - 1)
        if check(res, s, t):
            print("YES")
            print(res)
            return
        res = "a" + "b" * n + "c" * n + "a" * (n - 1)
        if check(res, s, t):
            print("YES")
            print(res)
            return
        res = "b" + "c" * n + "a" * n + "b" * (n - 1)
        if check(res, s, t):
            print("YES")
            print(res)
            return
        res = "c" + "a" * n + "b" * n + "c" * (n - 1)
        if check(res, s, t):
            print("YES")
            print(res)
            return
    
    if s[0] == s[1] and t[0] == t[1]:
        res = "abc" * n
        if check(res, s, t):
            print("YES")
            print(res)
            return
        res = "bac" * n
        if check(res, s, t):
            print("YES")
            print(res)
            return
        res = "cab" * n
        if check(res, s, t):
            print("YES")
            print(res)
            return
        res = "cba" * n
        if check(res, s, t):
            print("YES")
            print(res)
            return
        res = "bca" * n
        if check(res, s, t):
            print("YES")
            print(res)
            return
        res = "acb" * n
        if check(res, s, t):
            print("YES")
            print(res)
            return

    print("NO")

solve()