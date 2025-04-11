def schedule_exams(n, m, exams):
    days = [0] * n  # Initialize days with 0 (rest days)
    exam_days = set()  # To keep track of exam days
    prepare_needed = [0] * m  # To track preparation days needed for each exam

    # Fill exam days and preparation needs
    for i in range(m):
        s, d, c = exams[i]
        exam_days.add(d - 1)  # Store exam day (0-indexed)
        prepare_needed[i] = c

    # Prepare for exams
    for i in range(m):
        s, d, c = exams[i]
        s -= 1  # Convert to 0-indexed
        for j in range(s, d - 1):
            if prepare_needed[i] > 0 and days[j] == 0:
                days[j] = i + 1  # Mark preparation for exam i
                prepare_needed[i] -= 1

    # Check if all preparations are done
    for i in range(m):
        if prepare_needed[i] > 0:
            return -1  # Not enough days to prepare for exam i

    # Fill in exam days
    for i in range(m):
        d = exams[i][1] - 1  # Convert to 0-indexed
        days[d] = m + 1  # Mark exam day

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