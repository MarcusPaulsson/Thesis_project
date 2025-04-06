def solve():
    n, m = map(int, input().split())
    exams = []
    for i in range(m):
        s, d, c = map(int, input().split())
        exams.append((s, d, c, i + 1))

    schedule = [0] * n
    exam_days = {}
    for s, d, c, i in exams:
        exam_days[d - 1] = i

    for day in exam_days:
        schedule[day] = m + 1

    preparation_days = [0] * m
    
    for day in range(n):
        if schedule[day] == 0:
            best_exam = -1
            for s, d, c, i in exams:
                exam_index = i - 1
                if s - 1 <= day < d - 1 and preparation_days[exam_index] < c:
                    if best_exam == -1:
                        best_exam = exam_index
                    else:
                        s_best, d_best, c_best, i_best = exams[best_exam]
                        if d < d_best:
                            best_exam = exam_index
            
            if best_exam != -1:
                schedule[day] = exams[best_exam][3]
                preparation_days[best_exam] += 1

    possible = True
    for i in range(m):
        if preparation_days[i] != exams[i][2]:
            possible = False
            break

    if possible:
        print(*schedule)
    else:
        print(-1)

solve()