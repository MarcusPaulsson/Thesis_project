def schedule_exams(n, m, exams):
    schedule = [0] * n
    for i in range(m):
        s_i, d_i, c_i = exams[i]
        if d_i - s_i < c_i:
            return -1
        for j in range(s_i, d_i):
            if schedule[j] == 0:
                schedule[j] = i + 1
            elif schedule[j] != i + 1:
                return -1
    for i in range(m):
        s_i, d_i, c_i = exams[i]
        for j in range(s_i, s_i + c_i):
            if schedule[j] == 0:
                schedule[j] = i + 1
            elif schedule[j] != i + 1:
                return -1
    for i in range(n):
        if schedule[i] == 0:
            schedule[i] = m + 1
    return schedule

n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]
result = schedule_exams(n, m, exams)
if result == -1:
    print(-1)
else:
    print(*result)