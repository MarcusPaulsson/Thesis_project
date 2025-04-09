def is_s_palindrome(s):
    symmetric_chars = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p', 'o': 'o', 'x': 'x', 'X': 'X', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'Y': 'Y', 'A': 'A'}
    n = len(s)
    for i in range(n // 2):
        if s[i] not in symmetric_chars or s[n - 1 - i] not in symmetric_chars:
            return False
        if symmetric_chars.get(s[i]) != s[n - 1 - i]:
            return False
    if n % 2 == 1:
        if s[n // 2] not in symmetric_chars or symmetric_chars.get(s[n // 2]) != s[n // 2]:
            return False
    return True

s = input()
if is_s_palindrome(s):
    print("TAK")
else:
    print("NIE")