def solve():
    s = input()
    n = len(s)
    mirrors = {
        'b': 'd',
        'd': 'b',
        'o': 'o',
        'p': 'q',
        'q': 'p',
        'v': 'v',
        'w': 'w',
        'x': 'x',
        'A': 'A',
        'H': 'H',
        'I': 'I',
        'M': 'M',
        'O': 'O',
        'T': 'T',
        'U': 'U',
        'V': 'V',
        'W': 'W',
        'X': 'X',
        'Y': 'Y'
    }
    
    for i in range((n + 1) // 2):
        if s[i] not in mirrors or mirrors[s[i]] != s[n - 1 - i]:
            print("NIE")
            return
    
    print("TAK")

solve()