def solve():
    s = input()
    n = len(s)
    
    r_count = s.count('R')
    s_count = s.count('S')
    p_count = s.count('P')
    
    if r_count >= s_count and r_count >= p_count:
        print('P' * n)
    elif s_count >= r_count and s_count >= p_count:
        print('R' * n)
    else:
        print('S' * n)

t = int(input())
for _ in range(t):
    solve()