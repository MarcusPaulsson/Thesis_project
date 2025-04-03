def solve():
    s = input()
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j+1]
            length = j - i + 1
            try:
                val = int(sub, 2)
            except ValueError:
                val = 0
            if length == val:
                count += 1
    print(count)

t = int(input())
for _ in range(t):
    solve()