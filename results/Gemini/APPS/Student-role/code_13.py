def solve():
    n, g, b = map(int, input().split())
    
    required_good = (n + 1) // 2
    
    num_cycles = (required_good + g - 1) // g
    
    total_days = (num_cycles - 1) * (g + b) + required_good
    
    print(max(total_days, n))

t = int(input())
for _ in range(t):
    solve()