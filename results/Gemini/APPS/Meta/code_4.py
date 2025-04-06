def solve():
  x = int(input())
  hh, mm = map(int, input().split())

  def is_lucky(h, m):
    return '7' in str(h) or '7' in str(m)

  def time_to_minutes(h, m):
    return h * 60 + m

  def minutes_to_time(minutes):
    h = (minutes // 60) % 24
    m = minutes % 60
    return h, m

  target_minutes = time_to_minutes(hh, mm)
  
  for y in range(1000):
    alarm_minutes = (target_minutes - x * y) % (24 * 60)
    if alarm_minutes < 0:
      alarm_minutes += 24 * 60
    
    alarm_h, alarm_m = minutes_to_time(alarm_minutes)
    
    if is_lucky(alarm_h, alarm_m):
      print(y)
      return

solve()