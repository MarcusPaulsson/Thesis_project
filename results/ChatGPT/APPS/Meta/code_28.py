n = int(input())
files = [input().split() for _ in range(n)]

examples = []
regulars = []

# Separate examples and regular tests
for name, type_ in files:
    if type_ == '1':
        examples.append(name)
    else:
        regulars.append(name)

# Prepare the moves
moves = []
e = len(examples)

# Rename examples to 1, 2, ..., e
for i in range(e):
    moves.append(f"move {examples[i]} {i + 1}")

# Rename regular tests to e + 1, e + 2, ..., n
for i in range(len(regulars)):
    moves.append(f"move {regulars[i]} {e + i + 1}")

# Output the result
print(len(moves))
for move in moves:
    print(move)