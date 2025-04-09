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

    moves = []
    e = len(examples)
    r = len(regular)
    
    temps = []
    
    # Move examples to the front
    for i in range(e):
        if examples[i][0] != str(i + 1):
            temp_name = generate_temp_name(files)
            temps.append(temp_name)
            moves.append(f"move {examples[i][0]} {temp_name}")
            
            target_index = -1
            for j in range(n):
                if files[j][0] == str(i+1):
                    target_index = j
                    break
                    
            if target_index != -1:
                
                moves.append(f"move {str(i+1)} {str(e+r+len(temps))}")
                temps.append(str(e+r+len(temps)))
                moves.append(f"move {temp_name} {str(i+1)}")
                
                
                
                files[examples[i][1]][0] = str(i+1)
                files[target_index][0] = str(e+r+len(temps)-1)
                
                
                
            else:
                moves.append(f"move {temp_name} {str(i+1)}")
                files[examples[i][1]][0] = str(i+1)
                
    # Move regular tests to the back
    for i in range(r):
        if regular[i][0] != str(e + i + 1):
            
            temp_name = generate_temp_name(files)
            temps.append(temp_name)
            moves.append(f"move {regular[i][0]} {temp_name}")
            
            target_index = -1
            for j in range(n):
                if files[j][0] == str(e+i+1):
                    target_index = j
                    break
            
            if target_index != -1:
                moves.append(f"move {str(e+i+1)} {str(e+r+len(temps))}")
                temps.append(str(e+r+len(temps)))
                moves.append(f"move {temp_name} {str(e+i+1)}")
                
                files[regular[i][1]][0] = str(e+i+1)
                files[target_index][0] = str(e+r+len(temps)-1)
                
            else:
                moves.append(f"move {temp_name} {str(e+i+1)}")
                files[regular[i][1]][0] = str(e+i+1)

    print(len(moves))
    for move in moves:
        print(move)

def generate_temp_name(files):
    i = 1
    while True:
        temp_name = "temp" + str(i)
        exists = False
        for file in files:
            if file[0] == temp_name:
                exists = True
                break
        if not exists:
            return temp_name
        i += 1

solve()