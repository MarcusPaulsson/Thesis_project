def solve():
  n = int(input())
  a = list(map(int, input().split()))

  if n == 1:
    print(0)
    return

  unique_nums = sorted(list(set(a)))

  if len(unique_nums) > 3:
    print(-1)
    return
  
  if len(unique_nums) == 1:
    print(0)
    return

  if len(unique_nums) == 2:
    x, y = unique_nums
    if (x + y) % 2 == 0:
      print((y - x) // 2)
    else:
      print(y - x)
    return

  if len(unique_nums) == 3:
    x, y, z = unique_nums
    if y - x == z - y:
      print(y - x)
    else:
      print(-1)
    return

solve()