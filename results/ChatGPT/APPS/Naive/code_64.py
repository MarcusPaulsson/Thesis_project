def schedule_exams(n, m, exams):
    # Create a result list initialized with zeros
    result = [0] * n
    # To keep track of preparation days needed
    prepare_needed = [0] * m
    # To keep track of exam days
    exam_days = set()

    for idx, (s, d, c) in enumerate(exams):
        prepare_needed[idx] = c
        exam_days.add(d)

    # Prepare the days for exams
    for i in range(n):
        day = i + 1
        if day in exam_days:
            exam_index = next(idx for idx, (s, d, c) in enumerate(exams) if d == day)
            result[i] = exam_index + 1  # Exams are 1-indexed
            prepare_needed[exam_index] = max(0, prepare_needed[exam_index] - (day - exams[exam_index][0]))
        else:
            for exam_index in range(m):
                s, d, c = exams[exam_index]
                if s <= day < d and prepare_needed[exam_index] > 0:
                    result[i] = exam_index + 1  # Preparing for exam (1-indexed)
                    prepare_needed[exam_index] -= 1
                    break

    # Check if all preparation days were satisfied
    if any(c > 0 for c in prepare_needed):
        return -1

    return result

# Read input
n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

# Get the schedule
result = schedule_exams(n, m, exams)

# Print the result
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))