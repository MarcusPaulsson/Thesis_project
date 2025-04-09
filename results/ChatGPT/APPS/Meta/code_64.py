def schedule_exams(n, m, exams):
    days = [0] * n  # Initialize days with 0 (rest days)
    preparation_needed = [0] * m  # Track preparation days needed for each exam

    # Fill preparation_needed with the required preparation days
    for i in range(m):
        preparation_needed[i] = exams[i][2]

    # Check if we can allocate preparation days before each exam
    for i in range(m):
        s_i, d_i, c_i = exams[i]
        s_i -= 1  # Convert to 0-based index
        d_i -= 1  # Convert to 0-based index

        # Try to allocate the preparation days
        allocated_days = 0
        for day in range(s_i, d_i):
            if allocated_days < c_i and days[day] == 0:  # If we still need preparation days and the day is free
                days[day] = i + 1  # Mark this day for exam i
                allocated_days += 1

        # If we didn't allocate enough days, it's impossible
        if allocated_days < c_i:
            return -1

    # Now fill the exam days
    for i in range(m):
        d_i = exams[i][1] - 1  # Convert to 0-based index
        days[d_i] = m + 1  # Mark this day for the exam

    return days

# Reading input
n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

result = schedule_exams(n, m, exams)

if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))