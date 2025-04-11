def solve():
    n = int(input())
    s = input()
    t = input()

    chars = ['a', 'b', 'c']

    import itertools
    
    for perm in itertools.permutations(chars):
        base_string = "".join(perm)
        
        res = ""
        for _ in range(n):
            res += base_string
        
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
            
    print("NO")

solve()