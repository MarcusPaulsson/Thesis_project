n = int(input())
weeks = n // 7
rem = n % 7
min_days_off = weeks * 2
max_days_off = weeks * 2
if rem == 1:
    pass
elif rem == 2:
    max_days_off += 2
elif rem == 3:
    max_days_off += 2
elif rem == 4:
    max_days_off += 2
elif rem == 5:
    max_days_off += 2
elif rem == 6:
    max_days_off += 2
    min_days_off += 1

if rem == 1:
    pass
elif rem == 2:
    pass
elif rem == 3:
    min_days_off += 0
elif rem == 4:
    min_days_off += 0
elif rem == 5:
    min_days_off += 0
elif rem == 6:
    min_days_off += 1


if rem == 6 :
    min_days_off = weeks * 2 + 1
elif rem == 5:
    min_days_off = weeks*2
elif rem == 4:
    min_days_off = weeks*2
elif rem == 3:
    min_days_off = weeks*2
elif rem == 2:
    min_days_off = weeks*2
elif rem ==1:
    min_days_off = weeks*2
else:
    min_days_off = weeks*2

if rem == 6:
    max_days_off = weeks * 2 + 2
elif rem == 5:
    max_days_off = weeks * 2 + 2
elif rem == 4:
    max_days_off = weeks * 2 + 2
elif rem == 3:
    max_days_off = weeks * 2 + 2
elif rem == 2:
    max_days_off = weeks * 2 + 2
elif rem == 1:
    max_days_off = weeks * 2
else:
    max_days_off = weeks * 2
print(min_days_off, max_days_off)