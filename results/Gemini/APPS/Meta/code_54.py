def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(0)
        return

    for d in range(101):
        possible = False
        for target in range(1, 101):
            
            valid = True
            for x in a:
                if x == target:
                    continue
                elif x + d == target:
                    continue
                elif x - d == target:
                    continue
                else:
                    valid = False
                    break
            
            if valid:
                print(d)
                return
        
    print(-1)

solve()