def solve():
  """
  Calculates the minimum possible absolute difference between the sums of two sets
  formed by dividing the sequence 1, 2, ..., n.

  The problem is equivalent to checking if the sum of the sequence is even or odd.
  If the sum is even, the minimum difference is 0. Otherwise, it's 1.
  """
  n = int(input())
  total_sum = n * (n + 1) // 2  # Calculate the sum of the sequence efficiently
  print(total_sum % 2)  # Output 0 if even, 1 if odd

solve()