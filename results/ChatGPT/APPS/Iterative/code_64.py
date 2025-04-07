n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

# Initialize the schedule
schedule = [0] * n  # 0 means rest, will use 1 to m for exam prep and m+1 for exams

# Mark exam days
for i in range(m):
    s_i, d_i, c_i = exams[i]
    schedule[d_i - 1] = m + 1  # Exam day

# Prepare for exams
for i in range(m):
    s_i, d_i, c_i = exams[i]
    days_needed = c_i
    # Prepare for this exam in the available days
    for j in range(s_i - 1, d_i - 1):
        if schedule[j] == 0:  # Can only prepare on rest days
            schedule[j] = i + 1  # Mark as preparing for exam i
            days_needed -= 1
            if days_needed == 0:
                break
    
    if days_needed > 0:  # If we couldn't find enough days to prepare
        print(-1)
        exit()

# Print the final schedule
print(' '.join(map(str, schedule)))