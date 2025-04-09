def solve():
  n, m = map(int, input().split())
  exams = []
  for i in range(m):
    s, d, c = map(int, input().split())
    exams.append((s, d, c))
  
  schedule = [0] * n
  exam_days = {}
  for i in range(m):
    exam_days[exams[i][1] - 1] = i + 1
  
  for day in exam_days:
    schedule[day] = m + 1
    
  prep_counts = [0] * m
  
  for day in range(n):
    if schedule[day] == 0:
      best_exam = -1
      for i in range(m):
        s, d, c = exams[i]
        if s - 1 <= day < d - 1 and prep_counts[i] < c:
          if best_exam == -1:
            best_exam = i
          else:
            s_best, _, _ = exams[best_exam]
            if s > s_best:
              best_exam = i
      if best_exam != -1:
        schedule[day] = best_exam + 1
        prep_counts[best_exam] += 1
  
  for i in range(m):
    if prep_counts[i] != exams[i][2]:
      print("-1")
      return
  
  print(*schedule)

solve()