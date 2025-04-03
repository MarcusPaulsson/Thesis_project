def solve():
    n, g, b = map(int, input().split())
    
    required_good = (n + 1) // 2
    
    full_cycles = required_good // g
    remaining_good = required_good % g
    
    total_days = full_cycles * (g + b)
    
    if remaining_good > 0:
      total_days += remaining_good
    else:
      total_days -=b

    print(max(n, total_days))

t = int(input())
for _ in range(t):
    solve()