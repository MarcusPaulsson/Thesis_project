def is_palindrome(time):
  return time[0] == time[4] and time[1] == time[3]

def solve():
  time_str = input()
  hh = int(time_str[:2])
  mm = int(time_str[3:])

  minutes_slept = 0
  while True:
    if is_palindrome(f"{hh:02}:{mm:02}"):
      print(minutes_slept)
      return

    mm += 1
    if mm == 60:
      mm = 0
      hh += 1
      if hh == 24:
        hh = 0
    
    minutes_slept += 1

solve()