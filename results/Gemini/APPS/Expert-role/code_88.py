def solve():
    t = int(input())
    x = list(map(int, input().split()))
    
    for target in x:
        if target >= 14 and (target - 14) % 7 == 0:
            print("YES")
        else:
            print("NO")

solve()