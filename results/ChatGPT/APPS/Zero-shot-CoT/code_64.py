n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

# Prepare the schedule
schedule = [0] * n  # Initialize all days to rest (0)
exam_days = [0] * n  # To track which days are exam days

# Mark exam days
for i in range(m):
    s, d, c = exams[i]
    exam_days[d - 1] = i + 1  # Mark the exam day with the exam index (1-based)

# Prepare for exams
preparation_days = [0] * m  # Track how many days we have prepared for each exam
for i in range(n):
    if exam_days[i] != 0:
        exam_index = exam_days[i] - 1
        schedule[i] = exam_days[i]  # Mark exam day
    else:
        # Try to prepare for exams
        for j in range(m):
            s, d, c = exams[j]
            if s - 1 <= i < d - 1 and preparation_days[j] < c:
                schedule[i] = j + 1  # Mark preparation for exam j
                preparation_days[j] += 1
                break

# Check if all preparations are done
if all(preparation_days[j] == exams[j][2] for j in range(m)):
    print(" ".join(map(str, schedule)))
else:
    print(-1)