def is_palindrome(s):
  """Checks if a string is a palindrome."""
  return s == s[::-1]

def solve():
  """Finds the length of the longest non-palindrome substring."""
  s = input()
  n = len(s)

  if len(set(s)) == 1:
    print(0)
    return

  if not is_palindrome(s):
    print(n)
    return
  
  print(n - 1)

solve()