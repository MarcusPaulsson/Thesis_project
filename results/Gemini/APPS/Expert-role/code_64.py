def solve():
    n, m = map(int, input().split())
    exams = []
    for i in range(m):
        s, d, c = map(int, input().split())
        exams.append((s, d, c, i + 1))

    schedule = [0] * n
    exam_days = {}
    for i in range(m):
        exam_days[exams[i][1] - 1] = exams[i][3]

    for day, exam_num in exam_days.items():
        schedule[day] = m + 1

    prep_days_needed = [exam[2] for exam in exams]
    
    for day in range(n):
        if schedule[day] == 0:
            best_exam = -1
            for i in range(m):
                s, d, c, exam_num = exams[i]
                if s <= day + 1 and day + 1 < d and prep_days_needed[i] > 0:
                    best_exam = i
                    break
            
            if best_exam != -1:
                schedule[day] = exams[best_exam][3]
                prep_days_needed[best_exam] -= 1

    
    possible = True
    for i in range(m):
        if prep_days_needed[i] != 0:
            possible = False
            break

    if possible:
        print(*schedule)
    else:
        print("-1")

solve()