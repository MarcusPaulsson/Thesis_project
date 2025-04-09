def schedule_exams(n, m, exams):
    # Initialize the days array with zeros indicating rest days
    days = [0] * n
    exam_days = [0] * n  # To track the exam days
    
    # Prepare a list of exams with their respective indices for output
    exam_list = [(s, d, c, idx + 1) for idx, (s, d, c) in enumerate(exams)]
    
    # Sort exams by their exam day
    exam_list.sort(key=lambda x: x[1])
    
    # Allocate preparation days
    for s, d, c, idx in exam_list:
        available_days = [j for j in range(s - 1, d - 1) if days[j] == 0]  # Collect available rest days

        # Check if there are enough available days for preparation
        if len(available_days) < c:
            return -1
        
        # Schedule the preparation days
        for j in range(c):
            days[available_days[j]] = idx

        # Mark the exam day
        exam_days[d - 1] = idx

    # Fill exam days into the days array
    for i in range(n):
        if exam_days[i] != 0:
            days[i] = m + 1  # Mark exam days with (m + 1)

    return days

# Read input
n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

# Get the schedule
result = schedule_exams(n, m, exams)

# Print result
if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))