n = int(input())
files = [input().split() for _ in range(n)]

examples = [name for name, type_ in files if type_ == '1']
regulars = [name for name, type_ in files if type_ == '0']

moves = []
for i, name in enumerate(examples):
    moves.append(f"move {name} {i + 1}")

for i, name in enumerate(regulars):
    moves.append(f"move {name} {len(examples) + i + 1}")

print(len(moves))
print("\n".join(moves))