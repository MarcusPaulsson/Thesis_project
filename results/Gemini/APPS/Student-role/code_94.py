a, b, x = map(int, input().split())

if a > b:
  start = 0
else:
  start = 1

result = ""
while x > 1:
  result += str(start)
  if start == 0:
    b -= 1
    start = 1
  else:
    a -= 1
    start = 0
  x -= 1

if start == 0:
  result += "0" * a + "1" * b
else:
  result += "1" * b + "0" * a

print(result)