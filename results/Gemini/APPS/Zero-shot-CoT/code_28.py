def solve():
  n = int(input())
  files = []
  for _ in range(n):
    files.append(input().split())
  
  examples = []
  regular = []
  for i in range(n):
    if files[i][1] == '1':
      examples.append((files[i][0], i))
    else:
      regular.append((files[i][0], i))
      
  moves = []
  
  e = len(examples)
  
  temp_files = []
  
  for i in range(e):
    if examples[i][0] != str(i + 1):
      temp_files.append((examples[i][0], str(i + 1)))
      
  for i in range(len(regular)):
    if regular[i][0] != str(e + i + 1):
      temp_files.append((regular[i][0], str(e + i + 1)))
  
  
  
  
  conflicts = {}
  for i in range(e):
      if examples[i][0] != str(i+1):
          if str(i+1) in [x[0] for x in examples] or str(i+1) in [x[0] for x in regular]:
              continue
          else:
              moves.append(f"move {examples[i][0]} {str(i+1)}")
              
  for i in range(len(regular)):
    if regular[i][0] != str(e + i + 1):
      if str(e+i+1) in [x[0] for x in examples] or str(e+i+1) in [x[0] for x in regular]:
              continue
      else:
          moves.append(f"move {regular[i][0]} {str(e + i + 1)}")
          
  examples_left = []
  for i in range(e):
      if examples[i][0] != str(i+1):
          examples_left.append((examples[i][0], str(i+1)))
  
  regular_left = []
  for i in range(len(regular)):
    if regular[i][0] != str(e + i + 1):
        regular_left.append((regular[i][0], str(e + i + 1)))
  
  temp_names = []
  for i in range(len(examples_left) + len(regular_left)):
      temp_names.append("tmp" + str(i+1))
  
  temp_idx = 0
  for i in range(len(examples_left)):
      moves.append(f"move {examples_left[i][0]} {temp_names[temp_idx]}")
      temp_idx += 1
  
  for i in range(len(regular_left)):
      moves.append(f"move {regular_left[i][0]} {temp_names[temp_idx]}")
      temp_idx += 1
  
  temp_idx = 0
  for i in range(len(examples_left)):
      moves.append(f"move {temp_names[temp_idx]} {examples_left[i][1]}")
      temp_idx += 1
      
  for i in range(len(regular_left)):
      moves.append(f"move {temp_names[temp_idx]} {regular_left[i][1]}")
      temp_idx += 1
  
  print(len(moves))
  for move in moves:
    print(move)
    
solve()