def schedule_exams(n, m, exams):
    days = [0] * n  # Initialize days with 0 (rest days)
    preparation_needed = [0] * m  # Track preparation days needed for each exam
    exam_days = set()  # To track exam days

    # Populate exam days and needed preparation days
    for i in range(m):
        s, d, c = exams[i]
        preparation_needed[i] = c
        for day in range(s - 1, d - 1):  # Convert to 0-based index
            exam_days.add(day)

    # Check if we have enough days for preparation
    total_preparation_days = sum(preparation_needed)
    if total_preparation_days + m > n:  # Total days needed exceeds available days
        return -1

    # Prepare schedule
    for i in range(m):
        s, d, c = exams[i]
        preparation_days_count = 0
        
        # Try to allocate preparation days
        for day in range(s - 1, d - 1):  # Convert to 0-based index
            if preparation_days_count < c and days[day] == 0:  # Only prepare if it's a rest day
                days[day] = i + 1  # Mark day for preparation for exam i
                preparation_days_count += 1
        
        # Check if we allocated enough preparation days
        if preparation_days_count < c:
            return -1
    
    # Allocate exam days
    for i in range(m):
        d = exams[i][1]  # Get the exam day (1-based index)
        days[d - 1] = m + 1  # Mark the exam day (0-based index)

    return days

# Input reading
n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

# Get the result
result = schedule_exams(n, m, exams)

# Output result
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))