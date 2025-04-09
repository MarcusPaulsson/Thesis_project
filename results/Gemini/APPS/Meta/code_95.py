def solve():
    n = int(input())
    s = input()
    t = input()

    chars = ['a', 'b', 'c']

    import itertools

    for perm in itertools.permutations(chars):
        res = (perm[0] * n) + (perm[1] * n) + (perm[2] * n)
        
        s_found = False
        t_found = False
        
        for i in range(len(res) - 1):
            sub = res[i:i+2]
            if sub == s:
                s_found = True
            if sub == t:
                t_found = True
        
        if not s_found and not t_found:
            print("YES")
            print(res)
            return
            
    for perm in itertools.permutations(chars):
        res = (perm[0] * n) + (perm[2] * n) + (perm[1] * n)
        
        s_found = False
        t_found = False
        
        for i in range(len(res) - 1):
            sub = res[i:i+2]
            if sub == s:
                s_found = True
            if sub == t:
                t_found = True
        
        if not s_found and not t_found:
            print("YES")
            print(res)
            return

    for perm in itertools.permutations(chars):
        res = (perm[1] * n) + (perm[0] * n) + (perm[2] * n)
        
        s_found = False
        t_found = False
        
        for i in range(len(res) - 1):
            sub = res[i:i+2]
            if sub == s:
                s_found = True
            if sub == t:
                t_found = True
        
        if not s_found and not t_found:
            print("YES")
            print(res)
            return

    for perm in itertools.permutations(chars):
        res = (perm[1] * n) + (perm[2] * n) + (perm[0] * n)
        
        s_found = False
        t_found = False
        
        for i in range(len(res) - 1):
            sub = res[i:i+2]
            if sub == s:
                s_found = True
            if sub == t:
                t_found = True
        
        if not s_found and not t_found:
            print("YES")
            print(res)
            return

    for perm in itertools.permutations(chars):
        res = (perm[2] * n) + (perm[0] * n) + (perm[1] * n)
        
        s_found = False
        t_found = False
        
        for i in range(len(res) - 1):
            sub = res[i:i+2]
            if sub == s:
                s_found = True
            if sub == t:
                t_found = True
        
        if not s_found and not t_found:
            print("YES")
            print(res)
            return

    for perm in itertools.permutations(chars):
        res = (perm[2] * n) + (perm[1] * n) + (perm[0] * n)
        
        s_found = False
        t_found = False
        
        for i in range(len(res) - 1):
            sub = res[i:i+2]
            if sub == s:
                s_found = True
            if sub == t:
                t_found = True
        
        if not s_found and not t_found:
            print("YES")
            print(res)
            return
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    if n == 1:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        perm = ['a','b','c']
        res = "".join(perm)
        s_found = False
        t_found = False
        
        for i in range(len(res) - 1):
            sub = res[i:i+2]
            if sub == s:
                s_found = True
            if sub == t:
                t_found = True
        
        if not s_found and not t_found:
            print("YES")
            print(res)
            return
            
            
        perm = ['a','c','b']
        res = "".join(perm)
        s_found = False
        t_found = False
        
        for i in range(len(res) - 1):
            sub = res[i:i+2]
            if sub == s:
                s_found = True
            if sub == t:
                t_found = True
        
        if not s_found and not t_found:
            print("YES")
            print(res)
            return
            
            
            
        perm = ['b','a','c']
        res = "".join(perm)
        s_found = False
        t_found = False
        
        for i in range(len(res) - 1):
            sub = res[i:i+2]
            if sub == s:
                s_found = True
            if sub == t:
                t_found = True
        
        if not s_found and not t_found:
            print("YES")
            print(res)
            return
            
        perm = ['b','c','a']
        res = "".join(perm)
        s_found = False
        t_found = False
        
        for i in range(len(res) - 1):
            sub = res[i:i+2]
            if sub == s:
                s_found = True
            if sub == t:
                t_found = True
        
        if not s_found and not t_found:
            print("YES")
            print(res)
            return
            
        perm = ['c','a','b']
        res = "".join(perm)
        s_found = False
        t_found = False
        
        for i in range(len(res) - 1):
            sub = res[i:i+2]
            if sub == s:
                s_found = True
            if sub == t:
                t_found = True
        
        if not s_found and not t_found:
            print("YES")
            print(res)
            return
        
        perm = ['c','b','a']
        res = "".join(perm)
        s_found = False
        t_found = False
        
        for i in range(len(res) - 1):
            sub = res[i:i+2]
            if sub == s:
                s_found = True
            if sub == t:
                t_found = True
        
        if not s_found and not t_found:
            print("YES")
            print(res)
            return

solve()