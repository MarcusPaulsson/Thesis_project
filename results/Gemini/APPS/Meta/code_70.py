def solve():
  h1, m1 = map(int, input().split(':'))
  h2, m2 = map(int, input().split(':'))

  start_minutes = h1 * 60 + m1
  end_minutes = h2 * 60 + m2

  total_minutes = end_minutes - start_minutes
  midpoint_minutes = start_minutes + total_minutes // 2

  h3 = midpoint_minutes // 60
  m3 = midpoint_minutes % 60

  print("{:02d}:{:02d}".format(h3, m3))

solve()