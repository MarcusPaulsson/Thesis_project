def solve():
    n, m = map(int, input().split())
    exams = []
    for i in range(m):
        s, d, c = map(int, input().split())
        exams.append((s, d, c))

    schedule = [0] * n
    exam_days = {}
    for i in range(m):
        s, d, c = exams[i]
        exam_days[d - 1] = i + 1
        schedule[d - 1] = m + 1

    exam_preparations = [0] * m
    
    for day in range(n):
        if schedule[day] == 0:
            best_exam = -1
            for i in range(m):
                s, d, c = exams[i]
                if s - 1 <= day < d - 1 and exam_preparations[i] < c:
                    if best_exam == -1:
                        best_exam = i
                    else:
                        s_best, d_best, c_best = exams[best_exam]
                        if d < d_best:
                            best_exam = i
            
            if best_exam != -1:
                schedule[day] = best_exam + 1
                exam_preparations[best_exam] += 1
    
    possible = True
    for i in range(m):
        s, d, c = exams[i]
        if exam_preparations[i] != c:
            possible = False
            break

    if possible:
        print(*schedule)
    else:
        print(-1)

solve()