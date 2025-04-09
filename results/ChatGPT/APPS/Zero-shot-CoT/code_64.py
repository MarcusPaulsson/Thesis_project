def schedule_exams(n, m, exams):
    days = [0] * n
    needed_preparation = [0] * m
    preparation_days = [0] * m

    # Fill the days with exams
    for i in range(m):
        s_i, d_i, c_i = exams[i]
        needed_preparation[i] = c_i
        for day in range(s_i - 1, d_i - 1):
            if days[day] == 0:  # If the day is free
                preparation_days[i] += 1
                days[day] = i + 1  # Marking preparation for exam i+1

    # Check if preparation is sufficient
    if any(needed_preparation[i] > preparation_days[i] for i in range(m)):
        return -1

    # Now, mark the days for the exams
    for i in range(m):
        s_i, d_i, _ = exams[i]
        days[d_i - 1] = m + 1  # Mark the exam day

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