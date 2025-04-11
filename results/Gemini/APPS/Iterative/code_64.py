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
        schedule[d - 1] = m + 1
    
    preparation_counts = [0] * m
    
    for day in range(n):
        if schedule[day] == 0:
            best_exam = -1
            for s, d, c, i in exams:
                if s <= day + 1 < d and preparation_counts[i - 1] < c:
                    if best_exam == -1:
                        best_exam = i
            if best_exam != -1:
                schedule[day] = best_exam
                preparation_counts[best_exam - 1] += 1
    
    for i in range(m):
        if exams[i][2] != preparation_counts[i]:
            print(-1)
            return
    
    print(*schedule)

solve()