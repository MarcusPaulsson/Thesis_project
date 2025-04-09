def is_s_palindrome(s):
    """
    Checks if a string is an "s-palindrome".

    Args:
      s: The string to check.

    Returns:
      "TAK" if the string is an "s-palindrome", "NIE" otherwise.
    """

    mirrors = {
        'b': 'd', 'd': 'b',
        'p': 'q', 'q': 'p',
        'o': 'o', 'x': 'x',
        'X': 'X', 'H': 'H',
        'I': 'I', 'M': 'M',
        'O': 'O', 'T': 'T',
        'U': 'U', 'V': 'V',
        'v': 'v', 'W': 'W',
        'w': 'w', 'Y': 'Y',
        'A': 'A', 'm':'m'
    }

    n = len(s)
    for i in range(n // 2):
        if s[i] not in mirrors or mirrors[s[i]] != s[n - 1 - i]:
            return "NIE"
    
    if n % 2 == 1:
      if s[n//2] not in mirrors or mirrors[s[n//2]] != s[n//2]:
        return "NIE"

    return "TAK"


if __name__ == "__main__":
    s = input()
    print(is_s_palindrome(s))