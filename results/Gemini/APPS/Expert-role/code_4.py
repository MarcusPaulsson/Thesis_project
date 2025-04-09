def solve():
  x = int(input())
  hh, mm = map(int, input().split())

  def is_lucky(h, m):
    return '7' in str(h) or '7' in str(m)

  count = 0
  curr_hh = hh
  curr_mm = mm

  while not is_lucky(curr_hh, curr_mm):
    curr_mm -= x
    if curr_mm < 0:
      curr_hh -= 1
      curr_mm += 60
      if curr_hh < 0:
        curr_hh += 24
    count += 1

  print(count)

solve()