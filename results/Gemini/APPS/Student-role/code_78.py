def solve():
    n = int(input())
    s = input()
    mod = 10**9 + 7
    len_s = len(s)
    
    def is_regular(seq):
        balance = 0
        for char in seq:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    def count_regular_sequences(n, s):
        count = 0
        for i in range(2**(2*n)):
            seq = ""
            binary = bin(i)[2:].zfill(2*n)
            for bit in binary:
                if bit == '0':
                    seq += '('
                else:
                    seq += ')'
            
            if is_regular(seq) and s in seq:
                count = (count + 1) % mod
        return count

    print(count_regular_sequences(n, s))

solve()