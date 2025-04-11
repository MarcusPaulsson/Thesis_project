def schedule_exams(n, m, exams):
    days = [0] * n
    exam_days = set()

    for i in range(m):
        s, d, c = exams[i]
        exam_days.add(d - 1)  # Store exam days (0-indexed)

    preparation_days = [0] * m  # Count of preparation days for each exam
    for i in range(m):
        s, d, c = exams[i]
        for j in range(s - 1, d - 1):  # s-1 to d-2 (0-indexed)
            if preparation_days[i] < c and days[j] == 0:
                days[j] = i + 1  # Mark preparation for exam i
                preparation_days[i] += 1

    for i in range(m):
        if preparation_days[i] < exams[i][2]:  # If not enough preparation days
            return -1

    for i in range(n):
        if days[i] == 0:
            if i in exam_days:
                days[i] = m + 1  # Mark exam day
            else:
                days[i] = 0  # Rest day

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