def solve():
    n, m = map(int, input().split())
    exams = []
    for _ in range(m):
        s, d, c = map(int, input().split())
        exams.append((s, d, c))
    
    schedule = [0] * n
    exam_days = set()
    for s, d, _ in exams:
        exam_days.add(d)
    
    exam_prep_days = [0] * m
    
    def is_possible(exam_index, day):
        s, d, c = exams[exam_index]
        return s <= day < d
    
    def backtrack(day_index):
        if day_index == n:
            for i in range(m):
                if exam_prep_days[i] != exams[i][2]:
                    return False
            return True
        
        # Option 1: Rest
        schedule[day_index] = 0
        if backtrack(day_index + 1):
            return True
        
        # Option 2: Exam
        if day_index + 1 in exam_days:
            exam_index = -1
            for i in range(m):
                if exams[i][1] == day_index + 1:
                    exam_index = i
                    break
            if exam_index != -1:
                schedule[day_index] = m + 1
                if backtrack(day_index + 1):
                    return True
                schedule[day_index] = 0
        
        # Option 3: Prepare for an exam
        for i in range(m):
            if is_possible(i, day_index):
                schedule[day_index] = i + 1
                exam_prep_days[i] += 1
                if backtrack(day_index + 1):
                    return True
                exam_prep_days[i] -= 1
                schedule[day_index] = 0
        
        return False
    
    if backtrack(0):
        print(*schedule)
    else:
        print(-1)

solve()