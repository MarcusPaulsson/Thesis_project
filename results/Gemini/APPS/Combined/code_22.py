def solve():
    s = input()
    n = len(s)

    symmetric_chars = {
        'b': 'd', 'd': 'b',
        'p': 'q', 'q': 'p',
        'o': 'o', 'x': 'x',
        'v': 'v', 'w': 'w',
        'A': 'A', 'H': 'H',
        'I': 'I', 'M': 'M',
        'O': 'O', 'T': 'T',
        'U': 'U', 'V': 'V',
        'W': 'W', 'X': 'X',
        'Y': 'Y'
    }

    for i in range(n // 2):
        if s[i] not in symmetric_chars or symmetric_chars[s[i]] != s[n - 1 - i]:
            print("NIE")
            return

    if n % 2 == 1:
        mid_char = s[n // 2]
        if mid_char not in symmetric_chars or symmetric_chars[mid_char] != mid_char:
            print("NIE")
            return

    print("TAK")

solve()