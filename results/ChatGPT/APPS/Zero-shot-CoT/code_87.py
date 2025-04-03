def count_ambiguous_pairs(m, d, w):
    # The number of days in the year
    total_days = m * d
    
    # Calculate the number of ambiguous pairs
    ambiguous_count = 0
    
    # The number of full weeks in the year
    full_weeks = total_days // w
    
    # The number of days that align with weeks
    extra_days = total_days % w
    
    # We can only have ambiguous pairs for days that are within the bounds of the months
    days_limit = min(d, w)  # no day can exceed the days in a month or the week length
    
    for day in range(1, days_limit + 1):
        # Number of months that can contribute the same day of the week for the given day
        pairs_possible = (min(m, (w - day) // w + 1)) * (min(m, (w - day + 1) // w))
        
        ambiguous_count += pairs_possible
    
    return ambiguous_count

t = int(input())
results = []
for _ in range(t):
    m, d, w = map(int, input().split())
    results.append(count_ambiguous_pairs(m, d, w))

print('\n'.join(map(str, results)))