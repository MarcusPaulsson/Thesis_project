k = int(input())

digits = 1
count = 9
while k > digits * count:
  k -= digits * count
  digits += 1
  count *= 10

num = 10**(digits - 1) + (k - 1) // digits
index = (k - 1) % digits

print(str(num)[index])