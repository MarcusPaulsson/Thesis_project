def count_ambiguous_pairs(m, d, w):
    total_pairs = 0
    for month1 in range(1, m + 1):
        for month2 in range(month1 + 1, m + 1):
            # Calculate the day of the week for day month1 of month2
            day1 = (month1 - 1) * d + 1
            week_day1 = (day1 - 1) % w
            
            # Calculate the day of the week for day month2 of month1
            day2 = (month2 - 1) * d + 1
            week_day2 = (day2 - 1) % w
            
            # Check if the days are the same
            if week_day1 == week_day2:
                total_pairs += 1
    return total_pairs

t = int(input())
results = []
for _ in range(t):
    m, d, w = map(int, input().split())
    if w > d:
        w = d  # The effective week length cannot exceed the days in a month
    # Calculate the number of ambiguous pairs
    ambiguous_count = 0
    for x in range(1, min(m, d) + 1):
        for y in range(x + 1, m + 1):
            if (x - 1) // w % 2 == (y - 1) // w % 2:
                ambiguous_count += 1
    results.append(ambiguous_count)

print('\n'.join(map(str, results)))