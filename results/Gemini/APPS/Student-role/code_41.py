def nearest_zero(arr):
  """
  Finds the distance to the nearest zero for each element in the array.

  Args:
    arr: A list of integers.

  Returns:
    A list of integers representing the distances to the nearest zero.
  """

  n = len(arr)
  distances = [float('inf')] * n

  # Forward pass: find distances to the nearest zero from the left
  last_zero = float('-inf')
  for i in range(n):
    if arr[i] == 0:
      last_zero = i
    if last_zero != float('-inf'):
      distances[i] = min(distances[i], i - last_zero)

  # Backward pass: find distances to the nearest zero from the right
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
  distances = nearest_zero(arr)
  print(*distances)