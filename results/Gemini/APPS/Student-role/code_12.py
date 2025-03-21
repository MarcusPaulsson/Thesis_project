def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    possible = True
    
    for i in range(n):
        if a[i] == b[i]:
            continue
        
        if a[i] < b[i]:
            can_increase = False
            for j in range(i):
                if a[j] == 1:
                    can_increase = True
                    break
            if not can_increase:
                possible = False
                break
        else:
            can_decrease = False
            for j in range(i):
                if a[j] == -1:
                    can_decrease = True
                    break
            if not can_decrease:
                possible = False
                break

    if possible:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()