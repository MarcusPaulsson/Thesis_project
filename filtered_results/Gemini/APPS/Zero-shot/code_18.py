s = input()
n = len(s)
min_suffix = [0] * (n + 1)
min_suffix[n] = 'z'
for i in range(n - 1, -1, -1):
  min_suffix[i] = min(s[i], min_suffix[i + 1])
t = []
u = []
for i in range(n):
  t.append(s[i])
  while t and t[-1] <= min_suffix[i + 1]:
    u.append(t.pop())
while t:
  u.append(t.pop())
print(''.join(u))