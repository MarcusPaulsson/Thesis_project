def schedule_exams(n, m, exams):
    days = [0] * n
    exam_days = set()
    preparation_needed = [0] * m
    
    for i in range(m):
        s, d, c = exams[i]
        preparation_needed[i] = c
        exam_days.add(d - 1)  # Store exam days (0-indexed)
    
    for i in range(m):
        s, d, c = exams[i]
        prep_days = 0
        
        for j in range(s - 1, d - 1):  # s-1 to d-2 (0-indexed)
            if prep_days < c and days[j] == 0:
                days[j] = i + 1  # Mark preparation for exam i
                prep_days += 1
        
        if prep_days < c:
            return -1  # Not enough preparation days
    
    for i in range(n):
        if days[i] == 0 and i in exam_days:
            days[i] = m + 1  # Mark exam day
        elif days[i] == 0:
            days[i] = 0  # Rest day
    
    return days

# Input reading
n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

result = schedule_exams(n, m, exams)

if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))