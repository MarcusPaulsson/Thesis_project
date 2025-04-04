n, m = map(int, input().split())
exams = [list(map(int, input().split())) for _ in range(m)]
schedule = [0] * n  # Initialize the schedule with rest days (0)

# Mark exam days
for i in range(m):
    s, d, c = exams[i]
    schedule[d - 1] = m + 1  # Mark exam day with m + 1

# Prepare for exams
for i in range(m):
    s, d, c = exams[i]
    prepared_days = 0
    for j in range(s - 1, d - 1):  # From s_i to d_i - 1
        if prepared_days < c and schedule[j] == 0:  # Only prepare on rest days
            schedule[j] = i + 1  # Mark preparation day with exam number (1-indexed)
            prepared_days += 1
            
    # Check if we have prepared enough days
    if prepared_days < c:
        print(-1)
        exit()

# Print the final schedule
print(' '.join(map(str, schedule)))