s = input()
n = len(s)
symmetric = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p', 'o': 'o', 'x': 'x', 'X': 'X', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'T': 'T', 'U': 'U', 'V': 'V', 'v': 'v', 'W': 'W', 'w': 'w', 'Y': 'Y', 'A': 'A'}
flag = True
for i in range(n // 2):
    if s[i] not in symmetric or symmetric[s[i]] != s[n - i - 1]:
        flag = False
        break
if n % 2 == 1 and s[n // 2] not in symmetric:
    flag = False
if flag:
    print("TAK")
else:
    print("NIE")