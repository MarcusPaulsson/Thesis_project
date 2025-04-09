def schedule_exams(n, m, exams):
    days = [0] * n
    preparation_days = [0] * m
    exam_days = set()

    for i, (s, d, c) in enumerate(exams):
        exam_days.add(d - 1)
        if preparation_days[i] < c:
            for j in range(s - 1, d - 1):
                if preparation_days[i] < c and days[j] == 0:
                    days[j] = i + 1
                    preparation_days[i] += 1
    
    for i in range(m):
        if preparation_days[i] < exams[i][2]:
            return -1

    for i in range(n):
        if days[i] == 0 and i not in exam_days:
            days[i] = 0
        elif i in exam_days:
            days[i] = m + 1

    return days

n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]
result = schedule_exams(n, m, exams)

if result == -1:
    print(-1)
else:
    print(*result)