def solve():
    n = int(input())
    s = input()
    mod = 10**9 + 7
    
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
    
    def count_substring(seq, sub):
        count = 0
        for i in range(len(seq) - len(sub) + 1):
            if seq[i:i+len(sub)] == sub:
                count += 1
        return count > 0

    count = 0
    
    def generate_sequences(length):
        if length == 0:
            yield ""
        else:
            for seq in generate_sequences(length - 1):
                yield seq + "("
                yield seq + ")"
    
    for seq in generate_sequences(2 * n):
        if is_regular(seq) and count_substring(seq, s):
            count = (count + 1) % mod
    
    print(count)

solve()