def solve():
  n = int(input())
  s = input()

  def calculate_operations(target):
    count = 0
    i = 0
    while i < n:
      if s[i] != target[i % 2]:
        count += 1
        j = i
        while j < n and s[j] != target[i % 2]:
          j += 1
        i = j
      else:
        i += 1
    return count

  print(min(calculate_operations("01"), calculate_operations("10")))

t = int(input())
for _ in range(t):
  solve()