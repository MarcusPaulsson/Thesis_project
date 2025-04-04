def schedule_exams(n, m, exams):
    # Initialize the days array with zeros (rest days)
    days = [0] * n
    # Track the number of preparation days needed for each exam
    preparation_needed = [0] * m
    
    # Fill in the exam days in the schedule
    for idx, (s, d, c) in enumerate(exams):
        days[d - 1] = m + 1  # Exam day is marked with m + 1
        preparation_needed[idx] = c
    
    # Prepare for each exam
    for idx, (s, d, c) in enumerate(exams):
        count = 0
        for day in range(s - 1, d - 1):
            if days[day] == 0 and count < c:  # Only prepare if it's a rest day
                days[day] = idx + 1  # Mark the day for this exam's preparation
                count += 1
        
        if count < c:  # Not enough days to prepare for this exam
            return -1
    
    return days

# Input reading
n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

# Get the schedule
result = schedule_exams(n, m, exams)

# Output the result
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))