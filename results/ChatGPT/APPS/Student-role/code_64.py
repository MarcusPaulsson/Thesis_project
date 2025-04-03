n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

# Initialize the schedule with zeros (rest days)
schedule = [0] * n

# To track the preparation days needed for each exam
preparation_needed = [0] * m

# Mark exam days in the schedule
for i in range(m):
    s_i, d_i, c_i = exams[i]
    schedule[d_i - 1] = m + 1  # Mark the exam day

# Prepare for exams
for i in range(m):
    s_i, d_i, c_i = exams[i]
    days_to_prepare = []
    
    # Find available days for preparation
    for j in range(s_i - 1, d_i - 1):
        if schedule[j] == 0 and len(days_to_prepare) < c_i:
            days_to_prepare.append(j)
    
    # Check if we have enough days to prepare
    if len(days_to_prepare) < c_i:
        print(-1)
        exit()
    
    # Mark preparation days in the schedule
    for day in days_to_prepare:
        schedule[day] = i + 1  # Mark preparation for exam i+1

# Print the final schedule
print(' '.join(map(str, schedule)))