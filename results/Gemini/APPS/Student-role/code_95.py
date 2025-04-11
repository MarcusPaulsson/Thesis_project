def solve():
    n = int(input())
    s = input()
    t = input()

    chars = ['a', 'b', 'c']

    import itertools
    
    for perm in itertools.permutations(chars):
        res = ""
        for _ in range(n):
            res += "".join(perm)
        
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
    
    
    res1 = ""
    for _ in range(n):
        res1 += 'a'
    for _ in range(n):
        res1 += 'b'
    for _ in range(n):
        res1 += 'c'
    
    valid1 = True
    for i in range(len(res1) - 1):
        sub = res1[i:i+2]
        if sub == s or sub == t:
            valid1 = False
            break
    
    if valid1:
        print("YES")
        print(res1)
        return
    
    res2 = ""
    for _ in range(n):
        res2 += 'c'
    for _ in range(n):
        res2 += 'b'
    for _ in range(n):
        res2 += 'a'
    
    valid2 = True
    for i in range(len(res2) - 1):
        sub = res2[i:i+2]
        if sub == s or sub == t:
            valid2 = False
            break
    
    if valid2:
        print("YES")
        print(res2)
        return

    if n == 1:
        
        
        res = "abc"
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
        
        res = "acb"
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
        
        res = "bac"
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
        
        res = "bca"
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
        
        res = "cab"
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
        
        res = "cba"
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
    
    if n == 2:
        res = "acbacb"
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
    
    if n == 3:
        res = "acbacbacb"
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
    
    res = "abcabcabc"
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