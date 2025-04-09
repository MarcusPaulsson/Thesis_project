def solve():
  s = input()
  n = len(s)
  
  symmetric_chars = {
      'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p',
      'o': 'o', 'x': 'x', 'X': 'X', 'H': 'H',
      'I': 'I', 'M': 'M', 'O': 'O', 'T': 'T',
      'U': 'U', 'V': 'V', 'v': 'v', 'W': 'W',
      'w': 'w', 'Y': 'Y', 'A': 'A', 'i': 'i',
      'm': 'm', 'n': 'n'
  }
  
  is_s_palindrome = True
  for i in range(n // 2):
    if s[i] not in symmetric_chars or s[n - 1 - i] not in symmetric_chars:
      is_s_palindrome = False
      break
    if symmetric_chars.get(s[i]) != s[n - 1 - i]:
      is_s_palindrome = False
      break
  
  if n % 2 == 1:
    if s[n // 2] not in symmetric_chars:
       is_s_palindrome = False
  
  if is_s_palindrome:
    print("TAK")
  else:
    print("NIE")

solve()