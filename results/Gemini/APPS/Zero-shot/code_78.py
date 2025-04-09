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

    def generate_bracket_sequences(length):
        if length == 0:
            return [""]
        
        sequences = []
        for seq in generate_bracket_sequences(length - 1):
            sequences.append(seq + "(")
            sequences.append(seq + ")")
        return sequences
    
    all_sequences = generate_bracket_sequences(2 * n)
    
    count = 0
    for seq in all_sequences:
        if is_regular(seq) and s in seq:
            count = (count + 1) % mod
    
    print(count)

solve()