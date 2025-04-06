a, b, c = map(int, input().split())

possible = False
for i in range(c // a + 1):
  remaining_damage = c - i * a
  if remaining_damage >= 0 and remaining_damage % b == 0:
    possible = True
    break

if possible:
  print("Yes")
else:
  print("No")