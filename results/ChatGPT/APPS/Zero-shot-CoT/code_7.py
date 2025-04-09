def find_day_when_barn_empty(n, m):
    day = 0
    grains_in_barn = n
    
    while grains_in_barn > 0:
        day += 1
        grains_in_barn = min(grains_in_barn + m, n) - day
        
    return day

# Input
n, m = map(int, input().split())
print(find_day_when_barn_empty(n, m))