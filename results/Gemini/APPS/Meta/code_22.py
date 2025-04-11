def solve():
    s = input()
    n = len(s)
    
    mirror = {
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
        'A': 'A',
        'm':'m',
        't':'t',
        'u':'u',
        'y':'y'
    }
    
    for i in range(n // 2):
        if s[i] not in mirror or mirror[s[i]] != s[n - 1 - i]:
            print("NIE")
            return
    
    if n % 2 == 1:
        if s[n // 2] not in mirror or mirror[s[n // 2]] != s[n // 2]:
            print("NIE")
            return
    
    print("TAK")

solve()