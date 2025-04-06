def solve():
  n = int(input())
  tests = []
  for _ in range(n):
    tests.append(input().split())
  
  examples = []
  regular = []
  for i in range(n):
    if tests[i][1] == '1':
      examples.append(tests[i][0])
    else:
      regular.append(tests[i][0])
      
  moves = []
  
  e = len(examples)
  
  temp_files = set()
  
  
  for i in range(e):
    if examples[i] != str(i+1):
      while True:
        temp = "temp" + str(len(temp_files) + 1)
        if temp not in examples and temp not in regular:
          temp_files.add(temp)
          break
      moves.append(f"move {examples[i]} {temp}")
      examples[i] = temp
            
  for i in range(n - e):
    if regular[i] != str(e + i + 1):
      while True:
        temp = "temp" + str(len(temp_files) + 1)
        if temp not in examples and temp not in regular:
          temp_files.add(temp)
          break
      moves.append(f"move {regular[i]} {temp}")
      regular[i] = temp
  
  
  for i in range(e):
    if examples[i] != str(i+1):
      
      found = False
      for j in range(n-e):
        if regular[j] == str(i+1):
          
          while True:
            temp = "temp" + str(len(temp_files) + 1)
            if temp not in examples and temp not in regular:
              temp_files.add(temp)
              break
          moves.append(f"move {regular[j]} {temp}")
          regular[j] = temp
          
          moves.append(f"move {examples[i]} {str(i+1)}")
          examples[i] = str(i+1)
          found = True
          break
      if not found:
        moves.append(f"move {examples[i]} {str(i+1)}")
        examples[i] = str(i+1)
  
  for i in range(n-e):
    if regular[i] != str(e+i+1):
      moves.append(f"move {regular[i]} {str(e+i+1)}")
      regular[i] = str(e+i+1)
      
  print(len(moves))
  for move in moves:
    print(move)

solve()