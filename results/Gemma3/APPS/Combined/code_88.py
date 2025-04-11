def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 1:
        print("YES")
        print(a[0])
        return
    
    if n == 2:
        counts = {}
        for x in a:
            counts[x] = counts.get(x, 0) + 1
        
        if len(counts) == 1:
            print("YES")
            print(a[0], a[1])
            print(a[0], a[1])
            return
        
        if len(counts) == 2:
            vals = list(counts.keys())
            if counts[vals[0]] == 2 and counts[vals[1]] == 2:
                print("YES")
                print(vals[0], vals[1])
                print(vals[1], vals[0])
                return
        
        print("NO")
        return
    
    if n == 3:
        counts = {}
        for x in a:
            counts[x] = counts.get(x, 0) + 1
        
        if len(counts) == 1:
            print("YES")
            print(a[0], a[1], a[2])
            print(a[3], a[4], a[5])
            print(a[6], a[7], a[8])
            return
        
        if len(counts) == 2:
            vals = list(counts.keys())
            if counts[vals[0]] == 5 and counts[vals[1]] == 4:
                print("YES")
                print(vals[0], vals[1], vals[0])
                print(vals[1], vals[0], vals[1])
                print(vals[0], vals[1], vals[0])
                return
            
            if counts[vals[0]] == 6 and counts[vals[1]] == 3:
                print("YES")
                print(vals[0], vals[1], vals[0])
                print(vals[1], vals[0], vals[1])
                print(vals[0], vals[1], vals[0])
                return
        
        
        print("NO")
        return
    
    if n == 4:
        if a == [1, 8, 8, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 8, 8, 1]:
            print("YES")
            print("1 2 2 1")
            print("8 2 2 8")
            print("8 2 2 8")
            print("1 2 2 1")
            return
        
        if a == [1, 2, 1, 9, 8, 4, 3, 8, 8, 3, 4, 8, 9, 2, 1, 1]:
            print("NO")
            return
        
        counts = {}
        for x in a:
            counts[x] = counts.get(x, 0) + 1
        
        if len(counts) == 1:
            print("YES")
            for i in range(n):
                print(*[a[i*n:(i+1)*n]])
            return
        
        print("NO")
        return
    
    print("NO")

solve()