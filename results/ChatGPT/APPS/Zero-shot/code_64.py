def schedule_exams(n, m, exams):
    days = [0] * n
    exam_days = set()
    
    for i in range(m):
        s, d, c = exams[i]
        exam_days.add(d - 1)  # Store exam days (0-indexed)
    
    # Prepare for each exam
    for i in range(m):
        s, d, c = exams[i]
        prep_days = 0
        
        for j in range(s - 1, d - 1):  # s-1 to d-2 (0-indexed)
            if days[j] == 0 and prep_days < c:  # If it's a rest day and we need more prep days
                days[j] = i + 1  # Mark as preparing for exam i
                prep_days += 1
        
        if prep_days < c:  # If we couldn't prepare enough days
            return -1
    
    # Mark exam days
    for i in range(m):
        d = exams[i][1] - 1  # Exam day (0-indexed)
        days[d] = m + 1  # Mark as exam day
    
    return days

# Input reading
n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

# Get the schedule
result = schedule_exams(n, m, exams)

# Output result
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))