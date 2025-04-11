d, k, a, b, t = map(int, input().split())

if d <= k:
  print(d * a)
else:
  if t + k * a < k * b:
    rem = d - k
    num_breaks = rem // k
    ans = k * a + num_breaks * (t + k * a)
    rem = rem % k
    ans += min(t + rem * a, rem * b)
    print(ans)
  else:
    print(k * a + (d - k) * b)