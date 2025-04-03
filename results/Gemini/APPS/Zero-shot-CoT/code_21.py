def solve():
  n = int(input())
  a = list(map(int, input().split()))

  pos_1 = a.index(1)
  pos_n = a.index(n)

  ans = 0
  
  # Case 1: Swap 1 with the first element
  temp_a = a[:]
  temp_a[0], temp_a[pos_1] = temp_a[pos_1], temp_a[0]
  ans = max(ans, abs(temp_a.index(1) - temp_a.index(n)))

  # Case 2: Swap 1 with the last element
  temp_a = a[:]
  temp_a[n-1], temp_a[pos_1] = temp_a[pos_1], temp_a[n-1]
  ans = max(ans, abs(temp_a.index(1) - temp_a.index(n)))

  # Case 3: Swap n with the first element
  temp_a = a[:]
  temp_a[0], temp_a[pos_n] = temp_a[pos_n], temp_a[0]
  ans = max(ans, abs(temp_a.index(1) - temp_a.index(n)))

  # Case 4: Swap n with the last element
  temp_a = a[:]
  temp_a[n-1], temp_a[pos_n] = temp_a[pos_n], temp_a[n-1]
  ans = max(ans, abs(temp_a.index(1) - temp_a.index(n)))
  
  print(ans)

solve()