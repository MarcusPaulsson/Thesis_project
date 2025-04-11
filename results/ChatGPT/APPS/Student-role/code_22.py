def is_s_palindrome(s):
    mirror = {'A': 'A', 'B': ' ', 'C': ' ', 'D': ' ', 'E': ' ', 'F': ' ', 'G': ' ', 'H': 'H', 
              'I': 'I', 'J': ' ', 'K': ' ', 'L': ' ', 'M': 'M', 'N': ' ', 'O': 'O', 'P': ' ', 
              'Q': ' ', 'R': ' ', 'S': ' ', 'T': 'T', 'U': 'U', 'V': ' ', 'W': 'W', 'X': 'X', 
              'Y': ' ', 'Z': ' '}
    
    n = len(s)
    for i in range(n // 2):
        if mirror[s[i]] != s[n - 1 - i]:
            print("NIE")
            return
    print("TAK")

s = input().strip()
is_s_palindrome(s)