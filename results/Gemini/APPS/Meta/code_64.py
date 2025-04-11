def solve():
    n, m = map(int, input().split())
    exams = []
    for i in range(m):
        s, d, c = map(int, input().split())
        exams.append((s, d, c, i + 1))

    schedule = [0] * n
    exam_days = {}
    for i in range(m):
        s, d, c, exam_id = exams[i]
        exam_days[d] = exam_id

    for day in exam_days:
        schedule[day - 1] = m + 1

    preparation_counts = [0] * m
    
    for day in range(1, n + 1):
        if schedule[day - 1] == m + 1:
            continue
        
        best_exam = -1
        for i in range(m):
            s, d, c, exam_id = exams[i]
            if s <= day and day < d and preparation_counts[i] < c:
                if best_exam == -1:
                    best_exam = i
                else:
                    s_best, d_best, c_best, exam_id_best = exams[best_exam]
                    if d < d_best:
                        best_exam = i
        
        if best_exam != -1:
            schedule[day - 1] = exams[best_exam][3]
            preparation_counts[best_exam] += 1

    for i in range(m):
        if exams[i][2] != preparation_counts[i]:
            print("-1")
            return

    print(*schedule)

solve()