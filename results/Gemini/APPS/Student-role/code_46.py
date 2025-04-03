def solve():
    s = input()
    n = len(s)
    
    rock_count = s.count('R')
    scissors_count = s.count('S')
    paper_count = s.count('P')
    
    if rock_count >= scissors_count and rock_count >= paper_count:
        print('P' * n)
    elif scissors_count >= rock_count and scissors_count >= paper_count:
        print('R' * n)
    else:
        print('S' * n)

t = int(input())
for _ in range(t):
    solve()