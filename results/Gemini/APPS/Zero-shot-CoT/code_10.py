n = int(input())

min_days_off = n // 7 * 2
if n % 7 == 1:
    pass
elif n % 7 == 2:
    pass
elif n % 7 == 3:
    pass
elif n % 7 == 4:
    pass
elif n % 7 == 5:
    pass
elif n % 7 == 6:
    min_days_off += 0

max_days_off = n // 7 * 2
if n % 7 == 1:
    max_days_off += 1
elif n % 7 == 2:
    max_days_off += 2
elif n % 7 == 3:
    max_days_off += 2
elif n % 7 == 4:
    max_days_off += 2
elif n % 7 == 5:
    max_days_off += 2
elif n % 7 == 6:
    max_days_off += 2

if n % 7 == 6:
    min_days_off = n // 7 * 2 + 1
    if n % 7 > 0:
      if n % 7 >= 6:
        min_days_off = n // 7 * 2 + (n % 7) - 5 if (n//7 * 2 + (n%7) -5 ) > n//7 * 2 else n//7 *2
      else:
        min_days_off = n//7*2
elif n % 7 == 5:
    min_days_off = n // 7 * 2 + 0
elif n % 7 == 4:
  min_days_off = n // 7 * 2 + 0
elif n % 7 == 3:
  min_days_off = n // 7 * 2 + 0
elif n % 7 == 2:
  min_days_off = n // 7 * 2 + 0
elif n % 7 == 1:
  min_days_off = n // 7 * 2 + 0

if n <= 2:
  min_days_off = 0
  max_days_off = n
elif n <= 6:
  min_days_off = 0

print(min_days_off, max_days_off)