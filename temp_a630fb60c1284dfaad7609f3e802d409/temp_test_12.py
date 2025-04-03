def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(n):
        if a[i] == b[i]:
            continue
        elif a[i] < b[i]:
            found_pos = False
            for j in range(i):
                if a[j] == 1:
                    found_pos = True
                    break
            if not found_pos:
                print("NO")
                return
        else:
            found_neg = False
            for j in range(i):
                if a[j] == -1:
                    found_neg = True
                    break
            if not found_neg:
                print("NO")
                return
    print("YES")

t = int(input())
for _ in range(t):
    solve()