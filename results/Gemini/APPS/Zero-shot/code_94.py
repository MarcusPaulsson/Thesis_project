a, b, x = map(int, input().split())
s = ''
if a > b:
  start = '0'
  end = '1'
else:
  start = '1'
  end = '0'

s += start
a -= (start == '0')
b -= (start == '1')

for i in range(x - 1):
  if start == '0':
    if i % 2 == 0:
      s += '1'
      b -= 1
      start = '1'
    else:
      s += '0'
      a -= 1
      start = '0'
  else:
    if i % 2 == 0:
      s += '0'
      a -= 1
      start = '0'
    else:
      s += '1'
      b -= 1
      start = '1'

if start == '0':
  s += '0' * a
  s += '1' * b
else:
  s += '1' * b
  s += '0' * a

print(s)