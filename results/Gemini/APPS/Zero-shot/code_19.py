def solve():
  n = int(input())
  data = []
  for _ in range(n):
    data.append(list(map(int, input().split())))

  possible = True
  for i in range(n):
    if data[i][1] > data[i][0]:
      possible = False
      break
    if i > 0:
      if data[i][0] < data[i-1][0] or data[i][1] < data[i-1][1]:
        possible = False
        break
      if data[i][0] - data[i-1][0] < data[i][1] - data[i-1][1]:
        possible = False
        break

  if possible:
    print("YES")
  else:
    print("NO")


t = int(input())
for _ in range(t):
  solve()