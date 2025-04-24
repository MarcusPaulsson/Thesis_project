def solve():
    n, m = map(int, input().split())
    exams = []
    for i in range(m):
        s, d, c = map(int, input().split())
        exams.append((s, d, c))

    schedule = [0] * n

    # Mark exam days in the schedule
    for i in range(m):
        schedule[exams[i][1] - 1] = m + 1

    preparation_counts = [0] * m

    # Iterate through each day and assign preparation if possible
    for day in range(1, n + 1):
        if schedule[day - 1] != 0:  # Skip exam days
            continue

        best_exam = -1
        for i in range(m):
            s, d, c = exams[i]
            if s <= day and day < d and preparation_counts[i] < c:
                if best_exam == -1:
                    best_exam = i
                else:
                    # Prioritize exams with earlier deadlines
                    if exams[i][1] < exams[best_exam][1]:
                        best_exam = i

        if best_exam != -1:
            schedule[day - 1] = best_exam + 1
            preparation_counts[best_exam] += 1

    # Check if all exams have been prepared for enough days
    possible = True
    for i in range(m):
        if exams[i][2] != preparation_counts[i]:
            possible = False
            break

    if possible:
        print(*schedule)
    else:
        print("-1")

solve()