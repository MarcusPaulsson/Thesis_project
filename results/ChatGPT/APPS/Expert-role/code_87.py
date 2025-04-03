def count_ambiguous_pairs(m, d, w):
    # Calculate the number of days in the year
    total_days = m * d
    
    # Calculate the number of complete weeks in the total days
    complete_weeks = total_days // w
    
    # Calculate the number of extra days after complete weeks
    extra_days = total_days % w
    
    # Create a list to hold the count of days of the week
    days_count = [0] * w
    
    # Distribute the days across the weeks
    for i in range(w):
        days_count[i] = complete_weeks + (1 if i < extra_days else 0)
    
    # Calculate the number of ambiguous pairs
    ambiguous_pairs = 0
    
    # Count pairs (x, y) such that x < y
    for i in range(1, w):
        ambiguous_pairs += days_count[i] * days_count[i - 1]
    
    return ambiguous_pairs

t = int(input())
results = []
for _ in range(t):
    m, d, w = map(int, input().split())
    results.append(count_ambiguous_pairs(m, d, w))

print("\n".join(map(str, results)))