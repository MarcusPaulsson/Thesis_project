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
        schedule[d-1] = m + 1
    
    prep_counts = [0] * (m + 1)
    
    for day in range(n):
        if schedule[day] == m + 1:
            continue
        
        best_exam = -1
        for s, d, c, i in exams:
            if s <= day + 1 < d and prep_counts[i] < c:
                if best_exam == -1:
                    best_exam = i
                else:
                    
                    if d < exams[best_exam - 1][1]:
                        best_exam = i
        
        if best_exam != -1:
            schedule[day] = best_exam
            prep_counts[best_exam] += 1
    
    
    for s, d, c, i in exams:
        if prep_counts[i] != c:
            print("-1")
            return
    
    print(*schedule)

solve()