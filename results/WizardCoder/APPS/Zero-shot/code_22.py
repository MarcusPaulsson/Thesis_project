def minDigit(x):
    return int(str(x)[-1)

def maxDigit(x):
    return int(max(str(x))

for _ in range(int(input())):
    a, k = map(int, input().split())
    for i in range(2, k+1):
        a += minDigit(a)*maxDigit(a)
    print(a % 10**9)