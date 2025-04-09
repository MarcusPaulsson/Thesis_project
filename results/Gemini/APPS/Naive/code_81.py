def solve():
  n = int(input())
  strings = [input() for _ in range(n)]

  def is_substring(a, b):
    return a in b

  strings.sort(key=len)

  for i in range(1, n):
    for j in range(i):
      if not is_substring(strings[j], strings[i]):
        print("NO")
        return

  print("YES")
  for s in strings:
    print(s)

solve()