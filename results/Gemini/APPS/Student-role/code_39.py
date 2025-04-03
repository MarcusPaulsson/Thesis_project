def solve():
    a, b, p = map(int, input().split())
    s = input()
    n = len(s)

    for i in range(n):
        cost = 0
        curr = i
        while curr < n - 1:
            next_stop = curr + 1
            while next_stop < n - 1 and s[next_stop] == s[curr]:
                next_stop += 1
            
            if s[curr] == 'A':
                cost += a
            else:
                cost += b
            
            curr = next_stop
        
        if cost <= p:
            print(i + 1)
            return

t = int(input())
for _ in range(t):
    solve()