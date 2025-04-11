n = int(input())
files = [input().split() for _ in range(n)]

examples = [name for name, type_ in files if type_ == '1']
regulars = [name for name, type_ in files if type_ == '0']

moves = []
# Rename examples to 1, 2, ..., e
for i, example in enumerate(examples):
    moves.append(f"move {example} {i + 1}")

# Rename regular tests to e + 1, e + 2, ..., n
for i, regular in enumerate(regulars):
    moves.append(f"move {regular} {len(examples) + i + 1}")

print(len(moves))
for move in moves:
    print(move)