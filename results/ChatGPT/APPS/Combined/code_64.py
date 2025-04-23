def schedule_exams(n, m, exams):
    days = [0] * n  # Initialize days with 0 (rest)
    exam_days = [False] * (n + 1)  # Track exam days
    prepare_count = [0] * (m + 1)  # Track preparation days for each exam

    # Mark exam days
    for i in range(m):
        _, d_i, _ = exams[i]
        exam_days[d_i] = True

    # Prepare for exams
    for i in range(m):
        s_i, d_i, c_i = exams[i]
        prepared = 0
        
        for day in range(s_i - 1, d_i - 1):  # s_i to d_i - 1
            if prepared < c_i and days[day] == 0:  # If we need more preparation days and it's a rest day
                days[day] = i + 1  # Prepare for exam i
                prepared += 1
        
        if prepared < c_i:  # If we couldn't prepare enough days
            return -1

    # Assign exam days
    for i in range(m):
        _, d_i, _ = exams[i]
        days[d_i - 1] = m + 1  # Mark exam day

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