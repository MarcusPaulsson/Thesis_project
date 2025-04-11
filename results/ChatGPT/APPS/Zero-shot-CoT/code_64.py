def schedule_exams(n, m, exams):
    days = [0] * n
    exam_days = set()
    prepare_count = [0] * m

    for i in range(m):
        s_i, d_i, c_i = exams[i]
        exam_days.add(d_i - 1)  # d_i is 1-indexed, convert to 0-indexed
        prepare_count[i] = c_i

    # Check if we can fit the preparation days
    for i in range(m):
        s_i, d_i, c_i = exams[i]
        available_days = [j for j in range(s_i - 1, d_i - 1) if days[j] == 0]
        if len(available_days) < c_i:
            return -1  # Not enough days to prepare for this exam

        # Allocate preparation days
        for j in range(c_i):
            days[available_days[j]] = i + 1  # Mark preparation for exam i+1

    # Mark exam days
    for i in range(m):
        d_i = exams[i][1]
        days[d_i - 1] = m + 1  # Mark exam day

    return days

# Input reading
n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

result = schedule_exams(n, m, exams)
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))