def days_until_empty(n, m):
    day = 0
    total_grains = n
    
    while total_grains > 0:
        day += 1
        total_grains = min(total_grains + m, n) - day
        
    return day

n, m = map(int, input().split())
print(days_until_empty(n, m))