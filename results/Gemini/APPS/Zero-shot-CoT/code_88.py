def solve():
    t = int(input())
    x = list(map(int, input().split()))

    for target in x:
        if target < 14:
            print("NO")
            continue
        
        remaining = target - 14
        
        if remaining % 7 == 0:
            print("YES")
        else:
            print("YES")

solve()