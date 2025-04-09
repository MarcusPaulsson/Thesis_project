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
    
    # Move examples to 1, 2, ..., e
    for i in range(e):
        if examples[i][0] != str(i + 1):
            
            if any(f[0] == str(i+1) for f in examples) or any(f[0] == str(i+1) for f in regular):
                temp_name = generate_temp_name(files)
                moves.append(f"move {examples[i][0]} {temp_name}")
                
                # Find the file that should be moved to this position
                for j in range(n):
                    if files[j][0] == str(i+1):
                        if files[j][1] == '1':
                            moves.append(f"move {str(i+1)} {temp_name + '_temp'}")
                            moves.append(f"move {temp_name} {str(i+1)}")
                            moves.append(f"move {temp_name + '_temp'} {str(i+1)}")
                            
                        else:
                            moves.append(f"move {str(i+1)} {examples[i][0]}")
                            moves.append(f"move {temp_name} {str(i+1)}")
                        break
                else:
                    moves.append(f"move {temp_name} {str(i+1)}")
                

            else:
                moves.append(f"move {examples[i][0]} {str(i + 1)}")
    
    # Move regular tests to e+1, e+2, ..., n
    for i in range(len(regular)):
        if regular[i][0] != str(e + i + 1):
            
            if any(f[0] == str(e+i+1) for f in examples) or any(f[0] == str(e+i+1) for f in regular):
                temp_name = generate_temp_name(files)
                moves.append(f"move {regular[i][0]} {temp_name}")
                
                for j in range(n):
                    if files[j][0] == str(e+i+1):
                        if files[j][1] == '1':
                            moves.append(f"move {str(e+i+1)} {temp_name + '_temp'}")
                            moves.append(f"move {temp_name} {str(e+i+1)}")
                            moves.append(f"move {temp_name + '_temp'} {str(e+i+1)}")
                        else:
                            moves.append(f"move {str(e+i+1)} {regular[i][0]}")
                            moves.append(f"move {temp_name} {str(e+i+1)}")
                        break
                
                else:
                    moves.append(f"move {temp_name} {str(e + i + 1)}")

            else:
                moves.append(f"move {regular[i][0]} {str(e + i + 1)}")
    
    print(len(moves))
    for move in moves:
        print(move)

def generate_temp_name(files):
    temp_name = "temp1"
    i = 1
    while any(f[0] == temp_name for f in files):
        temp_name = f"temp{i}"
        i += 1
    return temp_name
    
solve()