def solve():
  n = int(input())
  records = []
  for _ in range(n):
    records.append(tuple(map(int, input().split())))

  for i in range(n):
    if records[i][1] > records[i][0]:
      print("NO")
      return

  for i in range(1, n):
    if records[i][0] < records[i-1][0] or records[i][1] < records[i-1][1]:
      print("NO")
      return
    
    if records[i][1] - records[i-1][1] > records[i][0] - records[i-1][0]:
      print("NO")
      return
  
  print("YES")


t = int(input())
for _ in range(t):
  solve()