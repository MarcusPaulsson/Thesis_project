def solve():
    n, m = map(int, input().split())
    exams = []
    for i in range(m):
        s, d, c = map(int, input().split())
        exams.append((s, d, c, i + 1))

    schedule = [0] * n
    exam_days = {}
    for s, d, c, i in exams:
        schedule[d - 1] = m + 1
        exam_days[d - 1] = i

    preparation_counts = [0] * m
    
    for day in range(n):
        if schedule[day] == m + 1:
            continue

        for i in range(m):
            s, d, c, exam_index = exams[i]
            if s <= day + 1 < d and preparation_counts[i] < c:
                schedule[day] = exam_index
                preparation_counts[i] += 1
                break

    for i in range(m):
        if preparation_counts[i] != exams[i][2]:
            print("-1")
            return

    print(*schedule)

solve()