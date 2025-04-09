def solve():
    n, m = map(int, input().split())
    exams = []
    for i in range(m):
        s, d, c = map(int, input().split())
        exams.append((s, d, c, i + 1))

    schedule = [0] * n
    exam_days = {}
    for s, d, c, i in exams:
        if d not in exam_days:
            exam_days[d] = i
        else:
            print("-1")
            return

    for day, exam_num in exam_days.items():
        schedule[day - 1] = m + 1

    preparation_days = [0] * m
    
    for day in range(n):
        if schedule[day] == 0:
            possible_exams = []
            for s, d, c, i in exams:
                if s <= day + 1 < d and preparation_days[i-1] < c:
                    possible_exams.append((i, s, d, c))
            
            best_exam = -1
            if(len(possible_exams) > 0):
              best_exam = possible_exams[0][0]
              schedule[day] = best_exam
              preparation_days[best_exam-1] += 1
                

    possible = True
    for s, d, c, i in exams:
        if preparation_days[i-1] != c:
            possible = False
            break
    
    if possible:
        print(*schedule)
    else:
        print("-1")

solve()