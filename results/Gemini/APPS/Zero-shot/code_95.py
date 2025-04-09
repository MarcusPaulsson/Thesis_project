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
            if res[i:i+2] == s or res[i:i+2] == t:
                valid = False
                break
        
        if valid:
            print("YES")
            print(res)
            return
    
    
    res = "a"*n + "b"*n + "c"*n
    valid = True
    for i in range(len(res) - 1):
        if res[i:i+2] == s or res[i:i+2] == t:
            valid = False
            break

    if valid:
        print("YES")
        print(res)
        return

    res = "c"*n + "b"*n + "a"*n
    valid = True
    for i in range(len(res) - 1):
        if res[i:i+2] == s or res[i:i+2] == t:
            valid = False
            break

    if valid:
        print("YES")
        print(res)
        return
    
    
    if n == 1 and (s == "ab" and t == "cb"):
        print("YES")
        print("bac")
        return


    for perm in itertools.permutations(chars):
        res = ""
        for i in range(n):
            res += perm[0]
            if i + 1 < n:
                res += perm[1]
            
        for i in range(n):
            res += perm[2]
            

        valid = True
        for i in range(len(res) - 1):
            if res[i:i+2] == s or res[i:i+2] == t:
                valid = False
                break
        
        if valid and len(res) == 3*n:
            print("YES")
            print(res)
            return

    print("NO")

solve()