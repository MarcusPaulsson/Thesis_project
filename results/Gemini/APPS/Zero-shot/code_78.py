def solve():
    n = int(input())
    s = input()
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
    
    def count_substring(seq, sub):
        count = 0
        for i in range(len(seq) - len(sub) + 1):
            if seq[i:i+len(sub)] == sub:
                count += 1
        return count
    
    def generate_bracket_sequences(length):
        if length == 0:
            return [""]
        
        sequences = []
        for sub_seq in generate_bracket_sequences(length - 1):
            sequences.append("(" + sub_seq)
            sequences.append(")" + sub_seq)
        return sequences
    
    all_sequences = generate_bracket_sequences(2 * n)
    
    count = 0
    for seq in all_sequences:
        if is_regular(seq) and count_substring(seq, s) > 0:
            count += 1
    
    print(count % (10**9 + 7))

solve()