def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(n):
        if a[i] == b[i]:
            continue
        
        if a[i] < b[i]:
            found_one = False
            for j in range(0, i):
                if a[j] == 1:
                    found_one = True
                    break
            if not found_one:
                print("NO")
                return
        else:
            found_minus_one = False
            for j in range(0, i):
                if a[j] == -1:
                    found_minus_one = True
                    break
            if not found_minus_one:
                print("NO")
                return

    print("YES")

t = int(input())
for _ in range(t):
    solve()