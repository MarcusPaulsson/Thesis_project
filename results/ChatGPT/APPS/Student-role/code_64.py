n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

schedule = [0] * n  # Initialize schedule with rest days
exam_days = [0] * n  # Initialize exam days tracker

for i in range(m):
    s, d, c = exams[i]
    s -= 1  # Convert to 0-based index
    d -= 1  # Convert to 0-based index
    exam_days[d] = i + 1  # Mark exam day

# Prepare a list to track preparation days
prep_days = [0] * n

for i in range(m):
    s, d, c = exams[i]
    s -= 1  # Convert to 0-based index
    d -= 1  # Convert to 0-based index
    count = 0
    
    # Try to assign preparation days
    for j in range(s, d):
        if count < c and prep_days[j] == 0:  # If we still need to prepare and the day is free
            prep_days[j] = i + 1  # Assign preparation for exam i
            count += 1

    if count < c:  # If we couldn't prepare enough
        print(-1)
        exit()

# Now fill the schedule with preparation and exam days
for j in range(n):
    if exam_days[j] != 0:
        schedule[j] = exam_days[j]  # Assign exam day
    elif prep_days[j] != 0:
        schedule[j] = prep_days[j]  # Assign preparation day

print(' '.join(map(str, schedule)))