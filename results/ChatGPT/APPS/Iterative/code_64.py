n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

# Prepare the schedule
schedule = [0] * n  # 0 means rest day
exam_days = set()

# Mark exam days
for i in range(m):
    s, d, c = exams[i]
    exam_days.add(d - 1)  # d is 1-based, convert to 0-based for index

# Prepare for exams
preparation_days = [0] * m
for i in range(m):
    s, d, c = exams[i]
    count = 0
    for day in range(s - 1, d - 1):
        if count < c and schedule[day] == 0:  # If it's a rest day
            schedule[day] = i + 1  # Mark preparation for exam i
            count += 1
    preparation_days[i] = count

# Check if all preparations are done
if any(preparation_days[i] < exams[i][2] for i in range(m)):
    print(-1)
else:
    # Fill exam days
    for i in range(m):
        d = exams[i][1] - 1
        schedule[d] = m + 1  # Mark exam day

    print(" ".join(map(str, schedule)))