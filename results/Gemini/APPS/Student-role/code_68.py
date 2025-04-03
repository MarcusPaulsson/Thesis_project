def solve():
  n = int(input())
  s = input()

  def calculate_operations(arr):
    operations = 0
    while arr:
      max_ops = 0
      best_i = -1

      for i in range(len(arr)):
        temp_arr = arr[:]
        del temp_arr[i]

        if not temp_arr:
          ops = 1
        else:
          first_char = temp_arr[0]
          j = 0
          while j < len(temp_arr) and temp_arr[j] == first_char:
            j += 1
          temp_arr = temp_arr[j:]
          ops = 1

        if ops > max_ops:
          max_ops = ops
          best_i = i

      del arr[best_i]
      operations += 1

      if arr:
        first_char = arr[0]
        j = 0
        while j < len(arr) and arr[j] == first_char:
          j += 1
        arr = arr[j:]

    return operations

  print(calculate_operations(list(s)))


t = int(input())
for _ in range(t):
  solve()