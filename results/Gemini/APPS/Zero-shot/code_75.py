a, b, c = map(int, input().split())

week = [0, 1, 2, 0, 2, 1, 0]
week_a = week.count(0)
week_b = week.count(1)
week_c = week.count(2)

weeks = min(a // week_a, b // week_b, c // week_c)

a -= weeks * week_a
b -= weeks * week_b
c -= weeks * week_c

ans = weeks * 7
max_days = 0

for start in range(7):
    temp_a, temp_b, temp_c = a, b, c
    days = 0
    
    for i in range(7):
        day_index = (start + i) % 7
        
        if week[day_index] == 0:
            if temp_a > 0:
                temp_a -= 1
                days += 1
            else:
                break
        elif week[day_index] == 1:
            if temp_b > 0:
                temp_b -= 1
                days += 1
            else:
                break
        else:
            if temp_c > 0:
                temp_c -= 1
                days += 1
            else:
                break
    
    max_days = max(max_days, days)

print(ans + max_days)