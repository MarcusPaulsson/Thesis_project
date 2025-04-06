def solve():
  n, r = map(int, input().split())
  projects = []
  for _ in range(n):
    projects.append(list(map(int, input().split())))

  import itertools
  for perm in itertools.permutations(projects):
    current_rating = r
    possible = True
    for project in perm:
      a, b = project
      if current_rating < a:
        possible = False
        break
      current_rating += b
      if current_rating < 0:
        possible = False
        break
    if possible:
      print("YES")
      return
  
  print("NO")

solve()