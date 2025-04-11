def schedule_exams(n, m, exams):
    days = [0] * n
    preparation_days = [0] * m

    # Sort exams by their exam day
    exams = sorted(enumerate(exams), key=lambda x: x[1][1])

    for index, (s, d, c) in exams:
        # Check if we can allocate preparation days
        available_days = [i for i in range(s - 1, d - 1) if days[i] == 0]
        
        if len(available_days) < c:
            return -1  # Not enough days to prepare
        
        # Allocate preparation days
        for i in range(c):
            days[available_days[i]] = index + 1  # Mark preparation for exam index + 1

        # Mark the exam day
        days[d - 1] = m + 1  # Mark the exam day

    return days

# Input reading
n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

# Get the schedule
result = schedule_exams(n, m, exams)

# Output result
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))