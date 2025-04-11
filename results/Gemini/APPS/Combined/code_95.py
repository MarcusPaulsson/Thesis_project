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

    res1 = "a" * n + "b" * n + "c" * n
    if check(res1, s, t):
        print("YES")
        print(res1)
        return

    res2 = "a" * n + "c" * n + "b" * n
    if check(res2, s, t):
        print("YES")
        print(res2)
        return

    res3 = "b" * n + "a" * n + "c" * n
    if check(res3, s, t):
        print("YES")
        print(res3)
        return

    res4 = "b" * n + "c" * n + "a" * n
    if check(res4, s, t):
        print("YES")
        print(res4)
        return

    res5 = "c" * n + "a" * n + "b" * n
    if check(res5, s, t):
        print("YES")
        print(res5)
        return

    res6 = "c" * n + "b" * n + "a" * n
    if check(res6, s, t):
        print("YES")
        print(res6)
        return

    res7 = "acb" * n
    if check(res7, s, t):
        print("YES")
        print(res7)
        return

    res8 = "bac" * n
    if check(res8, s, t):
        print("YES")
        print(res8)
        return

    res9 = "cba" * n
    if check(res9, s, t):
        print("YES")
        print(res9)
        return

    res10 = "abc" * n
    if check(res10, s, t):
        print("YES")
        print(res10)
        return
    
    res11 = "cab" * n
    if check(res11, s, t):
        print("YES")
        print(res11)
        return

    res12 = "bca" * n
    if check(res12, s, t):
        print("YES")
        print(res12)
        return

    print("NO")

solve()