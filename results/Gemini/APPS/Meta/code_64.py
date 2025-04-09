def solve():
    n, m = map(int, input().split())
    exams = []
    for i in range(m):
        s, d, c = map(int, input().split())
        exams.append((s, d, c))

    schedule = [0] * n
    exam_days = {}
    for i in range(m):
        exam_days[exams[i][1]] = i + 1
        schedule[exams[i][1] - 1] = m + 1

    prep_counts = [0] * m
    
    for day in range(1, n + 1):
        if schedule[day - 1] == m + 1:
            continue
        
        best_exam = -1
        
        for i in range(m):
            s, d, c = exams[i]
            
            if s <= day < d and prep_counts[i] < c:
                if best_exam == -1:
                    best_exam = i
                else:
                    s_best, d_best, c_best = exams[best_exam]
                    if d < d_best:
                        best_exam = i
                        
        if best_exam != -1:
            schedule[day - 1] = best_exam + 1
            prep_counts[best_exam] += 1

    possible = True
    for i in range(m):
        if prep_counts[i] != exams[i][2]:
            possible = False
            break

    if possible:
        print(*schedule)
    else:
        print(-1)

solve()