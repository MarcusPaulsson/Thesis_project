def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    possible = True
    
    for i in range(n):
        if a[i] == b[i]:
            continue
        
        if a[i] < b[i]:
            found_positive = False
            for j in range(i):
                if a[j] == 1:
                    found_positive = True
                    break
            if not found_positive:
                possible = False
                break
        else:
            found_negative = False
            for j in range(i):
                if a[j] == -1:
                    found_negative = True
                    break
            if not found_negative:
                possible = False
                break
    
    if possible:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()