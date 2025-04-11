def is_s_palindrome(s):
  """
  Checks if a string is an "s-palindrome".

  Args:
    s: The string to check.

  Returns:
    "TAK" if the string is an "s-palindrome", "NIE" otherwise.
  """

  s_palindrome_chars = {
      'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'T': 'T',
      'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'b': 'd',
      'd': 'b', 'o': 'o', 'p': 'q', 'q': 'p', 'v': 'v', 'w': 'w',
      'x': 'x'
  }

  n = len(s)
  for i in range(n // 2):
    if s[i] not in s_palindrome_chars or s[n - 1 - i] not in s_palindrome_chars:
      return "NIE"
    if s_palindrome_chars.get(s[i]) != s[n - 1 - i]:
      return "NIE"

  if n % 2 == 1:
    if s[n // 2] not in s_palindrome_chars or s_palindrome_chars.get(s[n // 2]) != s[n // 2]:
      return "NIE"

  return "TAK"


if __name__ == "__main__":
  s = input()
  print(is_s_palindrome(s))