def schedule_exams(n, m, exams):
    days = [0] * n
    preparation_needed = [0] * m
    exam_days = set()
    
    for i in range(m):
        s, d, c = exams[i]
        preparation_needed[i] = c
        for j in range(s - 1, d - 1):  # s-1 to d-2 (0-indexed)
            if days[j] == 0:
                days[j] = i + 1  # mark it for preparation

        exam_days.add(d - 1)  # mark the exam day

    for i in range(m):
        s, d, c = exams[i]
        count = 0
        for j in range(s - 1, d - 1):
            if days[j] == i + 1:
                count += 1
        if count < c:
            return -1
    
    for i in range(n):
        if i in exam_days:
            days[i] = m + 1  # exam day
    
    return days

# Input reading
n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

result = schedule_exams(n, m, exams)

if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))