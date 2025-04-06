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
  
  temps = []
  
  for i in range(e):
    if examples[i][0] != str(i+1):
      temps.append(str(n + 1 + len(temps)))
      moves.append(f"move {examples[i][0]} {temps[-1]} ")
  
  for i in range(e):
      if examples[i][0] != str(i+1):
          moves.append(f"move {temps[i]} {str(i+1)} ")
          
  for i in range(len(regular)):
      if regular[i][0] != str(e + i + 1):
          temps.append(str(n + 1 + len(temps)))
          moves.append(f"move {regular[i][0]} {temps[-1]} ")

  for i in range(len(regular)):
      if regular[i][0] != str(e + i + 1):
          moves.append(f"move {temps[e + i]} {str(e+i+1)} ")

  print(len(moves))
  for move in moves:
    print(move)

solve()