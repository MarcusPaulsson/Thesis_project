def solve():
    n, m = map(int, input().split())
    exams = []
    for i in range(m):
        s, d, c = map(int, input().split())
        exams.append((s, d, c, i + 1))

    schedule = [0] * n
    exam_days = {}
    for s, d, c, i in exams:
        if d in exam_days:
            print("-1")
            return
        exam_days[d] = i
        schedule[d - 1] = m + 1

    preparation_counts = [0] * m
    
    for day in range(n):
        if schedule[day] == 0:
            best_exam = -1
            for i in range(m):
                s, d, c, exam_num = exams[i]
                if s <= day + 1 < d and preparation_counts[i] < c:
                    if best_exam == -1:
                        best_exam = i
                    else:
                        s_best, d_best, c_best, exam_num_best = exams[best_exam]
                        if d < d_best:
                            best_exam = i
            
            if best_exam != -1:
                schedule[day] = exams[best_exam][3]
                preparation_counts[best_exam] += 1

    for i in range(m):
        if preparation_counts[i] != exams[i][2]:
            print("-1")
            return

    print(*schedule)

solve()