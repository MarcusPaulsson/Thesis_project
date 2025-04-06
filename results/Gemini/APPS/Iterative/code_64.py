def solve():
    n, m = map(int, input().split())
    exams = []
    for i in range(m):
        s, d, c = map(int, input().split())
        exams.append((s - 1, d - 1, c, i + 1))
    
    schedule = [0] * n
    exam_days = {}
    for s, d, c, i in exams:
        exam_days[d - 1] = i
        schedule[d - 1] = m + 1
    
    preparation = [0] * m
    
    for day in range(n):
        if schedule[day] == 0:
            best_exam = -1
            for s, d, c, i in exams:
                if s <= day < d and preparation[i-1] < c:
                    if best_exam == -1:
                        best_exam = i
                    else:
                        s_best, d_best, c_best, i_best = exams[best_exam - 1]
                        if d < d_best:
                            best_exam = i
                            
            if best_exam != -1:
                schedule[day] = best_exam
                preparation[best_exam - 1] += 1
    
    for s, d, c, i in exams:
        if preparation[i-1] != c:
            print(-1)
            return
    
    print(*schedule)

solve()