def solve():
    s = input()
    n = len(s)
    mirrors = {
        'b': 'd',
        'd': 'b',
        'p': 'q',
        'q': 'p',
        'o': 'o',
        'x': 'x',
        'X': 'X',
        'H': 'H',
        'I': 'I',
        'M': 'M',
        'O': 'O',
        'T': 'T',
        'U': 'U',
        'V': 'V',
        'v': 'v',
        'W': 'W',
        'w': 'w',
        'Y': 'Y',
        'y': 'y',
        'A': 'A',
    }
    
    for i in range((n + 1) // 2):
        if s[i] not in mirrors or mirrors[s[i]] != s[n - 1 - i]:
            print("NIE")
            return
    print("TAK")

solve()