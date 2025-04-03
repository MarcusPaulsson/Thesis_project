def solve():
  n = int(input())
  f = list(map(int, input().split()))

  assigned = [False] * (n + 1)
  for i in range(n):
    if f[i] != 0:
      assigned[f[i]] = True

  unassigned_givers = []
  unassigned_receivers = []
  for i in range(n):
    if f[i] == 0:
      unassigned_givers.append(i)

  for i in range(1, n + 1):
    if not assigned[i]:
      unassigned_receivers.append(i)

  for i in range(len(unassigned_givers)):
    giver_idx = unassigned_givers[i]
    receiver = unassigned_receivers[i]
    
    if giver_idx + 1 == receiver:
      if i + 1 < len(unassigned_givers):
        unassigned_receivers[i], unassigned_receivers[i+1] = unassigned_receivers[i+1], unassigned_receivers[i]
      else:
        for j in range(len(unassigned_givers)):
            if unassigned_givers[j] + 1 != unassigned_receivers[0] and j != i:
                unassigned_receivers[0], unassigned_receivers[i] = unassigned_receivers[i], unassigned_receivers[0]
                break


  for i in range(len(unassigned_givers)):
    f[unassigned_givers[i]] = unassigned_receivers[i]

  print(*f)

solve()