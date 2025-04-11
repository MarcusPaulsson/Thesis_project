n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

# Initialize the schedule with zeros (rest days)
schedule = [0] * n

# Prepare a list to track the preparation days needed for each exam
prep_days_needed = [0] * m

# Fill the schedule with exam days
for i in range(m):
    s_i, d_i, c_i = exams[i]
    schedule[d_i - 1] = m + 1  # Mark the exam day (1-indexed to 0-indexed)

    # Count the number of preparation days needed
    prep_days_needed[i] = c_i

# Try to allocate preparation days
for i in range(m):
    s_i, d_i, c_i = exams[i]
    days_allocated = 0

    # Allocate preparation days in the range [s_i, d_i - 1]
    for j in range(s_i - 1, d_i - 1):
        if days_allocated < c_i and schedule[j] == 0:
            schedule[j] = i + 1  # Mark preparation for exam i (1-indexed)
            days_allocated += 1

    # If we couldn't allocate enough preparation days, it's impossible
    if days_allocated < c_i:
        print(-1)
        exit()

# Print the final schedule
print(' '.join(map(str, schedule)))