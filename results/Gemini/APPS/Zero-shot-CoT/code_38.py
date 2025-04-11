def solve():
  n, l = map(int, input().split())
  kefa = list(map(int, input().split()))
  sasha = list(map(int, input().split()))

  for start in range(l):
    temp = []
    for i in range(n):
      temp.append((sasha[i] + start) % l)
    temp.sort()
    if temp == kefa:
      print("YES")
      return
  
  print("NO")

solve()