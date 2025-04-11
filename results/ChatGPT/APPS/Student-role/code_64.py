n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]
schedule = [0] * n

# Mark exam days
for i in range(m):
    s, d, c = exams[i]
    schedule[d - 1] = m + 1  # Mark the exam day

# Prepare for exams
for i in range(m):
    s, d, c = exams[i]
    prepare_days = 0
    for j in range(s - 1, d - 1):
        if prepare_days < c and schedule[j] == 0:
            schedule[j] = i + 1  # Mark preparation day
            prepare_days += 1

    if prepare_days < c:
        print(-1)
        exit()

print(" ".join(map(str, schedule)))