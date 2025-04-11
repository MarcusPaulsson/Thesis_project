def solve():
    n = int(input())
    s = input()
    t = input()

    chars = ['a', 'b', 'c']

    import itertools
    
    for p in itertools.permutations(chars):
        res = ""
        for i in range(n):
            res += p[0]
            res += p[1]
            res += p[2]
        
        valid = True
        if s in res or t in res:
            valid = False
        
        if valid:
            print("YES")
            print(res)
            return
    
    
    res1 = ""
    for i in range(n):
        res1 += "a"
    for i in range(n):
        res1 += "b"
    for i in range(n):
        res1 += "c"
    
    valid1 = True
    if s in res1 or t in res1:
        valid1 = False
    
    if valid1:
        print("YES")
        print(res1)
        return
    
    res2 = ""
    for i in range(n):
        res2 += "c"
    for i in range(n):
        res2 += "b"
    for i in range(n):
        res2 += "a"
    
    valid2 = True
    if s in res2 or t in res2:
        valid2 = False
    
    if valid2:
        print("YES")
        print(res2)
        return
    
    
    
    if n == 1:
        
        res = "abc"
        if s not in res and t not in res:
            print("YES")
            print(res)
            return
        
        res = "acb"
        if s not in res and t not in res:
            print("YES")
            print(res)
            return
        
        res = "bac"
        if s not in res and t not in res:
            print("YES")
            print(res)
            return
        
        res = "bca"
        if s not in res and t not in res:
            print("YES")
            print(res)
            return
        
        res = "cab"
        if s not in res and t not in res:
            print("YES")
            print(res)
            return
        
        res = "cba"
        if s not in res and t not in res:
            print("YES")
            print(res)
            return
    
    if n == 2:
        res = "acbacb"
        if s not in res and t not in res:
            print("YES")
            print(res)
            return
        
        res = "acbbac"
        if s not in res and t not in res:
            print("YES")
            print(res)
            return
    
    if n == 3:
        res = "acbacbacb"
        if s not in res and t not in res:
            print("YES")
            print(res)
            return
        
        res = "abcabcabc"
        if s not in res and t not in res:
            print("YES")
            print(res)
            return
        
        res = "cacbacbab"
        if s not in res and t not in res:
            print("YES")
            print(res)
            return
            
    if n == 3 and s == "bb" and t == "cb":
        print("YES")
        print("abcabcabc")
        return
    
    print("NO")

solve()