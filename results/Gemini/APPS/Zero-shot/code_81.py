def solve():
    a = input()
    b = input()
    c = input()
    n = len(a)
    
    for i in range(n):
        if (a[i] == c[i] and b[i] == c[i]):
            print("NO")
            return
        elif a[i] == c[i] and b[i] != c[i]:
            continue
        elif a[i] != c[i] and b[i] == c[i]:
            continue
        elif a[i] != c[i] and b[i] != c[i]:
            if a[i] != b[i]:
                continue
            else:
                print("NO")
                return
    print("YES")

t = int(input())
for _ in range(t):
    solve()