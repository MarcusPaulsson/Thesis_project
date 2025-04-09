def solve():
    n, x, y = map(int, input().split())
    s = input()
    
    count = 0
    for i in range(n - x, n):
        if i == n - 1 - y:
            if s[i] == '0':
                continue
            else:
                count += 1
        else:
            if s[i] == '1':
                continue
            else:
                count += 1
    print(count)

solve()