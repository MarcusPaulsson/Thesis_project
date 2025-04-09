def nearest_zero(arr):
  """
  Finds the distance to the nearest zero for each element in the array.

  Args:
    arr: A list of integers.

  Returns:
    A list of integers, where each element is the distance to the nearest zero.
  """

  n = len(arr)
  distances = [float('inf')] * n

  # Iterate from left to right
  last_zero = float('-inf')
  for i in range(n):
    if arr[i] == 0:
      last_zero = i
    if last_zero != float('-inf'):
      distances[i] = min(distances[i], i - last_zero)

  # Iterate from right to left
  last_zero = float('inf')
  for i in range(n - 1, -1, -1):
    if arr[i] == 0:
      last_zero = i
    if last_zero != float('inf'):
      distances[i] = min(distances[i], last_zero - i)

  return distances


if __name__ == "__main__":
  n = int(input())
  arr = list(map(int, input().split()))
  result = nearest_zero(arr)
  print(*result)