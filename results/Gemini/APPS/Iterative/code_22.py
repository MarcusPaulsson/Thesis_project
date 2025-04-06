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
        'A': 'A',
        'm': 'm',
        'Y': 'Y',

    }
    
    for i in range(n // 2):
        if s[i] not in mirrors or mirrors.get(s[i]) != s[n - 1 - i]:
            print("NIE")
            return
            
    if n % 2 == 1:
        if s[n // 2] not in mirrors or mirrors.get(s[n // 2]) != s[n // 2]:
            print("NIE")
            return
    
    print("TAK")
    
solve()