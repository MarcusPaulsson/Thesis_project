n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

# Schedule initialization
schedule = [0] * n  # 0 means rest day
exam_days = set()

# Mark exam days
for i in range(m):
    s, d, c = exams[i]
    exam_days.add(d - 1)  # d is 1-based, convert to 0-based
    schedule[d - 1] = m + 1  # m + 1 means an exam day

# Prepare days tracking
prepare_count = [0] * m

# Try to allocate preparation days
for day in range(n):
    if day in exam_days:
        continue  # Can't prepare on exam days
    for i in range(m):
        if prepare_count[i] < exams[i][2] and exams[i][0] - 1 <= day < exams[i][1] - 1:
            schedule[day] = i + 1  # Mark preparation for exam i
            prepare_count[i] += 1
            break

# Check if all preparations are satisfied
if all(prepare_count[i] == exams[i][2] for i in range(m)):
    print(' '.join(map(str, schedule)))
else:
    print(-1)