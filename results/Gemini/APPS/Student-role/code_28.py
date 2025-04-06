def solve():
    n = int(input())
    files = []
    for _ in range(n):
        files.append(input().split())
    
    examples = []
    regular = []
    for i in range(n):
        if files[i][1] == '1':
            examples.append((files[i][0], i))
        else:
            regular.append((files[i][0], i))
    
    e = len(examples)
    
    moves = []
    
    temp_files = []
    
    # Move examples to their correct positions
    for i in range(e):
        if examples[i][0] != str(i + 1):
            if str(i + 1) in [f[0] for f in examples] or str(i+1) in [f[0] for f in regular]:
                temp_name = generate_temp_name(files)
                temp_files.append(temp_name)
                moves.append(f"move {examples[i][0]} {temp_name}")
                moves.append(f"move {str(i+1)} {examples[i][0]}")
                moves.append(f"move {temp_name} {str(i+1)}")
            else:
                moves.append(f"move {examples[i][0]} {str(i+1)}")
    
    # Move regular files to their correct positions
    for i in range(len(regular)):
        if regular[i][0] != str(e + i + 1):
            if str(e + i + 1) in [f[0] for f in examples] or str(e+i+1) in [f[0] for f in regular]:
                temp_name = generate_temp_name(files)
                temp_files.append(temp_name)
                moves.append(f"move {regular[i][0]} {temp_name}")
                moves.append(f"move {str(e+i+1)} {regular[i][0]}")
                moves.append(f"move {temp_name} {str(e+i+1)}")
            else:
                moves.append(f"move {regular[i][0]} {str(e+i+1)}")
                
    print(len(moves))
    for move in moves:
        print(move)

def generate_temp_name(files):
    temp_name = "temp"
    i = 0
    while True:
        current_temp = temp_name + str(i)
        exists = False
        for file in files:
            if file[0] == current_temp:
                exists = True
                break
        if not exists:
            return current_temp
        i += 1

solve()