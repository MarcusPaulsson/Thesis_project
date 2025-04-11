def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(0)
        return

    for d in range(101):
        possible = True
        
        for target in set(a):
            
            valid = True
            for i in range(len(a)):
                found = False
                if a[i] == target:
                    found = True
                elif a[i] + d == target:
                    found = True
                elif a[i] - d == target:
                    found = True
                
                if not found:
                    valid = False
                    break
            
            if valid:
                print(d)
                return
        
    print(-1)

solve()