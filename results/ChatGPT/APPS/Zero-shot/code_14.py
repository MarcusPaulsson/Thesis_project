def schedule_exams(n, m, exams):
    days = [0] * n  # Initialize the schedule with rest days
    preparation_needed = [0] * m  # Preparation days needed for each exam
    preparation_slots = [[] for _ in range(m)]  # Slots to keep track of preparation days
    
    # Fill in the exam days in the schedule
    for i in range(m):
        s_i, d_i, c_i = exams[i]
        days[d_i - 1] = m + 1  # Mark the exam day
        preparation_needed[i] = c_i
        preparation_slots[i] = list(range(s_i - 1, d_i - 1))  # Possible preparation days

    # Try to allocate preparation days
    for i in range(m):
        needed = preparation_needed[i]
        for day in preparation_slots[i]:
            if needed == 0:
                break
            if days[day] == 0:  # If the day is free
                days[day] = i + 1  # Prepare for exam i
                needed -= 1
        
        if needed > 0:  # If we still need more preparation days
            return -1

    return days

# Read input
n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

# Get the schedule
result = schedule_exams(n, m, exams)

# Output the result
if result == -1:
    print(result)
else:
    print(' '.join(map(str, result)))