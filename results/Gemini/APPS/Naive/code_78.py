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

    def contains_substring(seq, sub):
        return sub in seq

    count = 0
    
    def generate_sequences(length):
      sequences = []
      def backtrack(current_sequence, open_count, close_count):
          if len(current_sequence) == length:
              sequences.append("".join(current_sequence))
              return
          
          if open_count < length // 2:
              current_sequence.append("(")
              backtrack(current_sequence, open_count + 1, close_count)
              current_sequence.pop()
          
          if close_count < open_count:
              current_sequence.append(")")
              backtrack(current_sequence, open_count, close_count + 1)
              current_sequence.pop()
      
      backtrack([], 0, 0)
      return sequences


    all_sequences = generate_sequences(2 * n)

    for seq in all_sequences:
        if is_regular(seq) and contains_substring(seq, s):
            count = (count + 1) % mod

    print(count)

solve()