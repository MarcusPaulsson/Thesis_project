n = int(input())
files = [input().split() for _ in range(n)]

examples = [f[0] for f in files if f[1] == '1']
regulars = [f[0] for f in files if f[1] == '0']

moves = []
# Move examples to 1 to e
for i, example in enumerate(examples):
    moves.append(f"move {example} {i + 1}")

# Move regulars to e + 1 to n
for i, regular in enumerate(regulars):
    moves.append(f"move {regular} {len(examples) + i + 1}")

print(len(moves))
print("\n".join(moves))