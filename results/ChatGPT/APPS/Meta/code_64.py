def schedule_exams(n, m, exams):
    days = [0] * n  # Initialize days with 0 (rest days)
    exam_days = [False] * (n + 1)  # Track exam days
    preparation_needed = [0] * (m + 1)  # Track preparation days needed for each exam

    # Fill exam days and preparation needs
    for i in range(m):
        s, d, c = exams[i]
        exam_days[d] = True
        preparation_needed[i + 1] = c

    # Prepare for exams
    for i in range(m):
        s, d, c = exams[i]
        count = 0
        for j in range(s, d):
            if count < c and days[j - 1] == 0:  # If we can prepare on this day
                days[j - 1] = i + 1  # Mark preparation for exam i+1
                count += 1
        if count < c:  # If we couldn't prepare enough days
            return -1

    # Assign exam days
    for i in range(m):
        d = exams[i][1]
        days[d - 1] = m + 1  # Mark exam day

    return days

# Input reading
n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

# Get the schedule
result = schedule_exams(n, m, exams)

# Output the result
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))