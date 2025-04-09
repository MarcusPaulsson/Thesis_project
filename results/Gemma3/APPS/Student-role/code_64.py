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
    
    def is_valid(schedule):
        for i in range(m):
            s, d, c = exams[i]
            prep_count = 0
            for j in range(s - 1, d - 1):
                if schedule[j] == i + 1:
                    prep_count += 1
            if prep_count != c:
                return False
        return True
    
    def can_schedule(index):
        if index == n:
            if is_valid(schedule):
                return True
            else:
                return False
        
        # Try rest
        schedule[index] = 0
        if can_schedule(index + 1):
            return True
        
        # Try exam
        if index + 1 in exam_days:
            exam_index = -1
            for i in range(m):
                if exams[i][1] == index + 1:
                    exam_index = i
                    break
            if exam_index != -1:
                schedule[index] = m + 1
                if can_schedule(index + 1):
                    return True
        
        # Try prepare for exam
        for i in range(m):
            s, d, c = exams[i]
            if s - 1 <= index < d - 1:
                if exam_prep_days[i] < c:
                    schedule[index] = i + 1
                    exam_prep_days[i] += 1
                    if can_schedule(index + 1):
                        return True
                    exam_prep_days[i] -= 1
        
        schedule[index] = 0
        return False
    
    if can_schedule(0):
        print(*schedule)
    else:
        print(-1)

solve()